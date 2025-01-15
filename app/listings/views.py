from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger  # noqa

from django.views.generic.detail import DetailView  # noqa
from .choices import foreman_choices, type_choices

from .models import Listing

# Extras
import pandas as pd
from django.shortcuts import redirect
from django.contrib import messages
from .forms import FileUploadForm
from foremen.models import Foreman
from django.db import IntegrityError


def index(request):
    """Docstring"""
    listings = Listing.objects.order_by('next_check').filter(is_active=True)

    paginator = Paginator(listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Docstring"""
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    """Docstring"""
    queryset_list = (
        Listing.objects.order_by('next_check')
        .filter(is_active=True)
    )

    # Tag
    if 'tag' in request.GET:
        tag = request.GET.get('tag')
        if tag:
            queryset_list = queryset_list.filter(tag__icontains=tag)

    # Type
    if 'type' in request.GET:
        type = request.GET.get('type')
        if type:
            queryset_list = queryset_list.filter(type__icontains=type)

    # Foreman
    if 'foreman' in request.GET:
        foreman = request.GET.get('foreman')
        if foreman:
            queryset_list = queryset_list.filter(foreman__name__iexact=foreman)

    context = {
        'foreman_choices': foreman_choices,
        'type_choices': type_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)


def bulk_import_listings(request):
    """Docstring for bulk_import_listings."""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            errors = []
            success_count = 0

            try:
                # Διαβάζουμε το αρχείο ανάλογα με τον τύπο του
                if file.name.endswith('.csv'):
                    data = pd.read_csv(file)
                elif file.name.endswith(('.xls', '.xlsx')):
                    data = pd.read_excel(file)
                else:
                    messages.error(request, "Unsupported file format.")
                    return redirect('bulk_import_listings')

                # Εισαγωγή δεδομένων και έλεγχος αν υπάρχει ήδη το tag
                for index, row in data.iterrows():
                    try:
                        foreman = Foreman.objects.get(id=row['foreman_id'])
                        if Listing.objects.filter(tag=row['tag']).exists():
                            errors.append(f"Row {index + 1}: Tag '{row['tag']}' already exists.")
                            continue

                        # Δημιουργία Listing αντικειμένου
                        Listing.objects.create(
                            foreman=foreman,
                            tag=row['tag'],
                            unit=row['unit'],
                            description=row['description'],
                            type=row['type'],
                            lrv=row['lrv'],
                            urv=row['urv'],
                            units=row['units'],
                            manufacturer=row.get('manufacturer', ''),
                            model=row.get('model', ''),
                            serial_no=row.get('serial_no', ''),
                            interval=row['interval'],
                            last_checked=pd.to_datetime(row['last_checked']),
                            is_active=row['is_active'],
                            history=row['history']
                        )
                        success_count += 1

                    except Foreman.DoesNotExist:
                        errors.append(f"Row {index + 1}: Foreman with ID '{row['foreman_id']}' not found.")
                    except IntegrityError as e:
                        errors.append(f"Row {index + 1}: Database error - {str(e)}.")
                    except Exception as e:
                        errors.append(f"Row {index + 1}: {str(e)}")

                # Εμφάνιση μηνυμάτων επιτυχίας και σφαλμάτων
                if success_count:
                    messages.success(request, f"Successfully imported {success_count} listings.")
                if errors:
                    for error in errors:
                        messages.warning(request, error)

                return redirect('bulk_import_listings')

            except Exception as e:
                messages.error(request, f"Error processing file: {e}")
    else:
        form = FileUploadForm()

    return render(request, 'listings/bulk_import.html', {'form': form})
