from datetime import date

from cleanWorld.models import cleans, placeImages, reports
from cleanWorld.upload import uploudImage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, UpdateView

from .forms import LoginForm, ProfileForm, ReportsForm, SignupForm
from .models import User
from .tokens import account_activation_token

# Create your views here.


def extentionValidator(name):
    charset = name.content_type
    exts = ['png', 'jpg', 'jpeg']
    try:
        if charset.split('/')[-1] in exts:
            return True
        return False
    except:
        return False


@login_required
def dashboard(request, page=1):

    user_reoprts = reports.objects.filter(
        reporter=request.user).order_by('cleanedStatus', '-reportedAt')
    user_cleans = cleans.objects.filter(cleaner=request.user)
    all_reminded_reports = reports.objects.filter(cleanedStatus=False)
    all_reports = reports.objects.all()

    paginator = Paginator(user_reoprts, 10)
    dirty = paginator.get_page(page)

    context = {
        'current_year': date.today().year,
        'user_reports': user_reoprts,
        'user_cleans': user_cleans,
        'all_reminded_reports': all_reminded_reports,
        'all_reports': all_reports,
        'dirty': dirty
    }

    return render(request, 'registration/dashboard.html',  context=context)


@login_required
def makeClean(request, pk):
    try:
        reportObj = reports.objects.get(pk=pk)
    except:
        context = {
            'title': 'گزارش مورد نظر شما یافت نشد!',
            'message': 'این گزارش وجود ندارد.',
            'type': 'danger',
            'current_year': date.today().year,
        }
        return render(request, 'registration/registration_messages.html', context=context)
    else:
        reportObj.cleanedStatus = True
        reportObj.save()

        try:
            cleanObj = cleans(cleaner=request.user, report=reportObj)
            cleanObj.save()
        except:
            context = {
                'title': 'گزارش مورد نظر شما قبلا پاکیزه شده است!',
                'message': 'این گزارش وجود ندارد.',
                'type': 'danger',
                'current_year': date.today().year,
            }
            return render(request, 'registration/registration_messages.html', context=context)
        else:
            context = {
                'title': 'ممنون از همکاری شما',
                'message': 'اکنون شما در پاکیزه تر شدن زمین سهیم هستید.',
                'type': 'success',
                'current_year': date.today().year,
            }
            return render(request, 'registration/registration_messages.html', context=context)


@login_required
def dirtyAddress(request, coordinates):
    context = {
        'title': 'مکان موردنظر یافت نشد',
        'message': 'این مکان در لیست گزارشات وجود ندارد.',
        'type': 'danger',
    }
    try:
        dirtyPlace = reports.objects.filter(
            coordinates=coordinates, cleanedStatus=False)
    except:
        return render(request, 'registration/registration_messages.html', context=context)

    if not dirtyPlace:
        return render(request, 'registration/registration_messages.html', context=context)
    else:
        context = {
            'coordinates': coordinates,
            'current_year': date.today().year,
            'dirtyPlace': dirtyPlace[0],
        }
        return render(request, 'registration/google_map_address.html', context=context)


@login_required
def dirtyPlaces(request, page=1):
    dirty_list = reports.objects.filter(
        cleanedStatus=False).order_by('-reportedAt')

    paginator = Paginator(dirty_list, 10)
    dirty = paginator.get_page(page)

    context = {
        'current_year': date.today().year,
        'dirty': dirty,
    }

    return render(request, 'registration/dirtyPlaces.html',  context=context)


class Report(LoginRequiredMixin, CreateView):
    form_class = ReportsForm
    template_name = 'registration/report.html'
    extra_context = {
        'current_year': date.today().year,
    }

    def get_context_data(self, **kwargs):
        context = super(Report, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def form_valid(self, form):
        form_data = form.cleaned_data
        if reports.objects.filter(
            coordinates=form_data.get('coordinates'),
            cleanedStatus=False
        ).exists():
            messages.add_message(self.request, messages.INFO,
                                 'این مکان در لیست مکان های آلوده وجود دارد.')
            return HttpResponseRedirect(self.request.path_info)

        reportObj = reports.objects.create(
            reporter=self.request.user,
            coordinates=form_data.get('coordinates'),
            address=form_data.get('address')
        )
        reportObj.garbageType.set(form_data.get('garbageType'))

        images = self.request.FILES.getlist('images')
        if len(images) > 6:
            reportObj.delete()
            messages.add_message(self.request, messages.ERROR,
                                 'شما مجاز به آپلود حداکثر 6 عکس میباشید.')
            return HttpResponseRedirect(self.request.path_info)
        images_pk = []
        for image in images:
            if extentionValidator(image):
                obj = placeImages.objects.create(
                    image=image, user=self.request.user)
                images_pk.append(obj.pk)

                local = '.' + obj.image.url
                dest = '/' + obj.image.url.split('images/')[1]
                url = uploudImage(local, dest)
                if url:
                    obj.imageUrl = url
                    obj.save()
            else:
                reportObj.delete()
                messages.add_message(
                    self.request, messages.ERROR, 'لطفا فقط فایل با پسوند های PNG, JPG, JPEG آپلود کنید.')
                return HttpResponseRedirect(self.request.path_info)

        reportObj.images.set(images_pk)

        context = {
            'title': 'ممنون از مشارکت شما',
            'message': 'محل موردنظر شما با موفقیت ثبت شد',
            'type': 'success',
        }
        return render(self.request, 'registration/registration_messages.html', context=context)


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class Login(LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True


class Register(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:dashboard')
        return super(Register, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی حساب کاربری'
        print(user.pk, urlsafe_base64_encode(force_bytes(user.pk)))
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'page_title': 'فعالسازی حساب'
        })
        to_email = form.cleaned_data.get('email')
        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(
            mail_subject, message, email_from, to=[to_email]
        )
        email.content_subtype = 'html'
        email.send()

        context = {
            'title': 'ثبت نام',
            'message': 'لینک فعال سازی برای شما ارسال شد. برای فعالسازی ایمیل خود را چک کنید اگر ایمیل را دریافت نکرده اید بخش Spam را چک کنید.',
            'type': 'success'
        }
        return render(self.request, 'registration/registration_messages.html', context=context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        context = {
            'title': 'ثبت نام',
            'message': 'حساب کاربری شما با موفقیت فعال شد اکنون میتوانید وارد حساب کاربری خود شوید.',
            'type': 'success',
            'redirect': 'login'
        }
        return render(request, 'registration/registration_messages.html', context=context)
    else:
        context = {
            'title': 'ثبت نام',
            'message': 'این لینک منقضی شده است.',
            'type': 'danger',
            'redirect': 'login'
        }
        return render(request, 'registration/registration_messages.html', context=context)


@login_required
def userProfile(request, pk):
    if not User.objects.filter(pk=pk):
        context = {
            'title': 'کاربر یافت نشد!',
            'message': 'کاربر موردنظر یافت نشد.',
            'type': 'danger',
        }
        return render(request, 'registration/registration_messages.html', context=context)
    else:
        user = User.objects.get(pk=pk)
        reportsObj = reports.objects.filter(reporter=user)
        cleansObj = cleans.objects.filter(cleaner=user)

        context = {
            'reports': reportsObj.count(),
            'cleans': cleansObj.count(),
            'reporter': user,
            'current_year': date.today().year,
        }
        return render(request, 'registration/reporterProfile.html', context=context)


@login_required
def removeReport(request, pk):
    if not reports.objects.filter(reporter=request.user, pk=pk):
        context = {
            'title': 'گزارش یافت نشد!',
            'message': 'شما چنین گزارشی را ثبت نکرده اید.',
            'type': 'danger',
            'current_year': date.today().year,
        }
        return render(request, 'registration/registration_messages.html', context=context)
    else:

        user = request.user
        reportsObj = reports.objects.filter(reporter=user, pk=pk)
        reportsObj.delete()

        context = {
            'title': 'حذف گزارش',
            'message': 'گزارش شما با موفقیت حذف شد!',
            'type': 'success',
            'current_year': date.today().year,
        }
        return render(request, 'registration/registration_messages.html', context=context)


@login_required
def CleanerProfile(request, pk):
    if not cleans.objects.filter(report_id=pk):
        context = {
            'title': 'گزارش یافت نشد!',
            'message': 'گزارش موردنظر یافت نشد.',
            'type': 'danger',
        }
        return render(request, 'registration/registration_messages.html', context=context)
    else:
        cleansObj = cleans.objects.get(report_id=pk)
        user = cleansObj.cleaner

        reportsObj = reports.objects.filter(reporter=user)
        cleansObj = cleans.objects.filter(cleaner=user)

        context = {
            'reports': reportsObj.count(),
            'cleans': cleansObj.count(),
            'cleaner': user,
            'current_year': date.today().year,
        }
        return render(request, 'registration/CleanerProfile.html', context=context)
