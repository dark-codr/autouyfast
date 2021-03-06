from __future__ import absolute_import

# development system imports
import datetime
import os
import random
import uuid
from datetime import timedelta
from decimal import Decimal
from urllib import request

# Third partie imports
from category.models import Category, Tag
from comment.models import Comment
from countries_plus.models import Country
# django imports
from django.conf import settings
from django.core.files import File
from django.core.mail import BadHeaderError, EmailMessage, send_mail, send_mass_mail
from django.db.models import (
    CASCADE,
    SET_NULL,
    BigIntegerField,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    ManyToManyField,
    OneToOneField,
    PositiveSmallIntegerField,
    SlugField,
    TextChoices,
    TextField,
    URLField,
    UUIDField,
)
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
# Third party installs
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField

from .managers import CarManager


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def post_image(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "cars/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )
def car_vid_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "cars/video/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename
    )

User = settings.AUTH_USER_MODEL

CAR_MAKE = (
    ('all', 'all'),
    ('ac', 'ac'),
    ('acura', 'acura'),
    ('alfa_romeo', 'alfa romeo'),
    ('allard', 'allard'),
    ('amc', 'amc'),
    ('am_general', 'am general'),
    ('american_motors', 'american motors'),
    ('ariel', 'ariel'),
    ('aston_martin', 'aston martin'),
    ('auburn', 'auburn'),
    ('audi', 'audi'),
    ('austin', 'austin'),
    ('austin_healey', 'austin healey'),
    ('avantimotors', 'avantimotors'),
    ('bentley', 'bentley'),
    ('bmw', 'bmw'),
    ('bugatti', 'bugatti'),
    ('buick', 'buick'),
    ('cadillac', 'cadillac'),
    ('checker', 'checker'),
    ('chevrolet', 'chevrolet'),
    ('chrysler', 'chrysler'),
    ('citroen', 'citroen'),
    ('daewoo', 'daewoo'),
    ('daihatsu', 'daihatsu'),
    ('datsun', 'datsun'),
    ('delahaye', 'delahaye'),
    ('delorean', 'delorean'),
    ('desoto', 'desoto'),
    ('detomaso', 'detomaso'),
    ('dodge', 'dodge'),
    ('eagle', 'eagle'),
    ('edsel', 'edsel'),
    ('essex', 'essex'),
    ('ferrari', 'ferrari'),
    ('fiat', 'fiat'),
    ('fisker', 'fisker'),
    ('ford', 'ford'),
    ('franklin', 'franklin'),
    ('freightliner', 'freightliner'),
    ('genesis', 'genesis'),
    ('geo', 'geo'),
    ('gmc', 'gmc'),
    ('hino', 'hino'),
    ('honda', 'honda'),
    ('hudson', 'hudson'),
    ('hummer', 'hummer'),
    ('hupmobile', 'hupmobile'),
    ('hyundai', 'hyundai'),
    ('infiniti', 'infiniti'),
    ('international', 'international'),
    ('intlharvester', 'intlharvester'),
    ('isuzu', 'isuzu'),
    ('jaguar', 'jaguar'),
    ('jeep', 'jeep'),
    ('jensen', 'jensen'),
    ('kaiser', 'kaiser'),
    ('karma', 'karma'),
    ('kia', 'kia'),
    ('koenigsegg', 'koenigsegg'),
    ('lamborghini', 'lamborghini'),
    ('lancia', 'lancia'),
    ('land_rover', 'land rover'),
    ('lasalle', 'lasalle'),
    ('lexus', 'lexus'),
    ('lincoln', 'lincoln'),
    ('lotus', 'lotus'),
    ('maserati', 'maserati'),
    ('maybach', 'maybach'),
    ('mazda', 'mazda'),
    ('mclaren', 'mclaren'),
    ('mercedes_benz', 'mercedes benz'),
    ('mercury', 'mercury'),
    ('merkur', 'merkur'),
    ('mg', 'mg'),
    ('mini', 'mini'),
    ('mitsubishi', 'mitsubishi'),
    ('morgan', 'morgan'),
    ('morris', 'morris'),
    ('nash', 'nash'),
    ('nissan', 'nissan'),
    ('oldsmobile', 'oldsmobile'),
    ('opel', 'opel'),
    ('packard', 'packard'),
    ('pagani', 'pagani'),
    ('panoz', 'panoz'),
    ('peugeot', 'peugeot'),
    ('plymouth', 'plymouth'),
    ('polestar', 'polestar'),
    ('pontiac', 'pontiac'),
    ('porsche', 'porsche'),
    ('qvale', 'qvale'),
    ('ram', 'ram'),
    ('renault', 'renault'),
    ('rolls_royce', 'rollsroyce'),
    ('rover', 'rover'),
    ('saab', 'saab'),
    ('saleen', 'saleen'),
    ('saturn', 'saturn'),
    ('scion', 'scion'),
    ('shelby', 'shelby'),
    ('smart', 'smart'),
    ('spyker', 'spyker'),
    ('sterling', 'sterling'),
    ('studebaker', 'studebaker'),
    ('subaru', 'subaru'),
    ('sunbeam', 'sunbeam'),
    ('suzuki', 'suzuki'),
    ('tesla', 'tesla'),
    ('toyota', 'toyota'),
    ('triumph', 'triumph'),
    ('tvr', 'tvr'),
    ('volkswagen', 'volkswagen'),
    ('volvo', 'volvo'),
    ('willys', 'willys'),
    ('yugo', 'yugo'),
)
CAR_STOCK = (
    ('Used', 'used'),
    ('New', 'new'),
    ('Certified', 'certified'),
    ('Acura_Certified', 'acura'),
    ('Alfa_Romeo _Certified', 'alfa romeo'),
    ('Allard_Certified', 'allard'),
    ('Amc_Certified', 'amc'),
    ('Am_General_Certified', 'am general'),
    ('American_Motors_Certified', 'american motors'),
    ('Ariel_Certified', 'ariel'),
    ('Aston_Martin_Certified', 'aston martin'),
    ('Auburn_Certified', 'auburn'),
    ('Audi_Certified', 'audi'),
    ('Austin_Certified', 'austin'),
    ('Austin_Healey_Certified', 'austin healey'),
    ('Avantimotors_Certified', 'avantimotors'),
    ('Bentley_Certified', 'bentley'),
    ('BMW_Certified', 'bmw'),
    ('Bugatti_Certified', 'bugatti'),
    ('Buick_Certified', 'buick'),
    ('Cadillac_Certified', 'cadillac'),
    ('Checker_Certified', 'checker'),
    ('Chevrolet_Certified', 'chevrolet'),
    ('Chrysler_Certified', 'chrysler'),
    ('Citroen_Certified', 'citroen'),
    ('Daewoo_Certified', 'daewoo'),
    ('Daihatsu_Certified', 'daihatsu'),
    ('Datsun_Certified', 'datsun'),
    ('Delahaye_Certified', 'delahaye'),
    ('Delorean_Certified', 'delorean'),
    ('Desoto_Certified', 'desoto'),
    ('Detomaso_Certified', 'detomaso'),
    ('Dodge_Certified', 'dodge'),
    ('Eagle_Certified', 'eagle'),
    ('Edsel_Certified', 'edsel'),
    ('Essex_Certified', 'essex'),
    ('Ferrari_Certified', 'ferrari'),
    ('Fiat_Certified', 'fiat'),
    ('Fisker_Certified', 'fisker'),
    ('Ford_Certified', 'ford'),
    ('Franklin_Certified', 'franklin'),
    ('Freightliner_Certified', 'freightliner'),
    ('Genesis_Certified', 'genesis'),
    ('GEO_Certified', 'geo'),
    ('GMC_Certified', 'gmc'),
    ('Hino_Certified', 'hino'),
    ('Honda_Certified', 'honda'),
    ('Hudson_Certified', 'hudson'),
    ('Hummer_Certified', 'hummer'),
    ('Hupmobile_Certified', 'hupmobile'),
    ('Hyundai_Certified', 'hyundai'),
    ('INFINITI_Certified', 'infiniti'),
    ('International_Certified', 'international'),
    ('Intlharvester_Certified', 'intlharvester'),
    ('Isuzu_Certified', 'isuzu'),
    ('Jaguar_Certified', 'jaguar'),
    ('Jeep_Certified', 'jeep'),
    ('Jensen_Certified', 'jensen'),
    ('Kaiser_Certified', 'kaiser'),
    ('Karma_Certified', 'karma'),
    ('Kia_Certified', 'kia'),
    ('Koenigsegg_Certified', 'koenigsegg'),
    ('Lamborghini_Certified', 'lamborghini'),
    ('Lancia_Certified', 'lancia'),
    ('Land_Rover_Certified', 'land rover'),
    ('Lasalle_Certified', 'lasalle'),
    ('Lexus_Certified', 'lexus'),
    ('Lincoln_Certified', 'lincoln'),
    ('Lotus_Certified', 'lotus'),
    ('Maserati_Certified', 'maserati'),
    ('Maybach_Certified', 'maybach'),
    ('Mazda_Certified', 'mazda'),
    ('Mclaren_Certified', 'mclaren'),
    ('Mercedes_Benz_Certified', 'mercedes benz'),
    ('Mercury_Certified', 'mercury'),
    ('Merkur_Certified', 'merkur'),
    ('MG_Certified', 'mg'),
    ('Mini_Certified', 'mini'),
    ('Mitsubishi_Certified', 'mitsubishi'),
    ('Morgan_Certified', 'morgan'),
    ('Morris_Certified', 'morris'),
    ('Nash_Certified', 'nash'),
    ('Nissan_Certified', 'nissan'),
    ('Oldsmobile_Certified', 'oldsmobile'),
    ('Opel_Certified', 'opel'),
    ('Packard_Certified', 'packard'),
    ('Pagani_Certified', 'pagani'),
    ('Panoz_Certified', 'panoz'),
    ('Peugeot_Certified', 'peugeot'),
    ('Plymouth_Certified', 'plymouth'),
    ('Polestar_Certified', 'polestar'),
    ('Pontiac_Certified', 'pontiac'),
    ('Porsche_Certified', 'porsche'),
    ('Qvale_Certified', 'qvale'),
    ('RAM_Certified', 'ram'),
    ('Renault_Certified', 'renault'),
    ('Rolls Royce_Certified', 'rollsroyce'),
    ('Rover_Certified', 'rover'),
    ('Saab_Certified', 'saab'),
    ('Saleen_Certified', 'saleen'),
    ('Saturn_Certified', 'saturn'),
    ('Scion_Certified', 'scion'),
    ('Ehelby_Certified', 'shelby'),
    ('Smart_Certified', 'smart'),
    ('Spyker_Certified', 'spyker'),
    ('Sterling_Certified', 'sterling'),
    ('Studebaker_Certified', 'studebaker'),
    ('Subaru_Certified', 'subaru'),
    ('Sunbeam_Certified', 'sunbeam'),
    ('Suzuki_Certified', 'suzuki'),
    ('Tesla_Certified', 'tesla'),
    ('Toyota_Certified', 'toyota'),
    ('Triumph_Certified', 'triumph'),
    ('Tvr_Certified', 'tvr'),
    ('Volkswagen_Certified', 'volkswagen'),
    ('Volvo_Certified', 'volvo'),
    ('Willys_Certified', 'willys'),
    ('Yugo_Certified', 'yugo'),
)
CAR_YEAR = (
    (2000, 2000),
    (2001, 2001),
    (2002, 2002),
    (2003, 2003),
    (2004, 2004),
    (2005, 2005),
    (2006, 2006),
    (2007, 2007),
    (2008, 2008),
    (2009, 2009),
    (2010, 2010),
    (2011, 2011),
    (2012, 2012),
    (2013, 2013),
    (2014, 2014),
    (2015, 2015),
    (2016, 2016),
    (2017, 2017),
    (2018, 2018),
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
)

CAR_DOOR = (
    ('all', 'all'),
    ('2', '2-3'),
    ('4', '4'),        
)
CAR_BODY = (
    ('all', 'all'),
    ('sedan', 'sedan'),
    ('coupe', 'coupe'),
    ('convertible', 'convertible'),
    ('wagon', 'wagon'),
    ('hatchback', 'hatchback'),
    ('passenger_van', 'passenger van'),
    ('suv', 'suv'),
    ('minivan', 'minivan'),
    ('pickup_truck', 'pickup truck'),
    ('cargo_van', 'cargo van'),
)

class AutoSearch(TimeStampedModel):
    UNPUBLISHED = "unpublished"
    PUBLISHED = "published"
    STATUS = (
        (UNPUBLISHED, "unpublished"),
        (PUBLISHED, "published")
    )
    title = CharField(_("Car Title"), max_length=700, blank=True, null=True, unique=False) 
    slug = SlugField(max_length=800, blank=True, null=True, unique=True)
    car_url = CharField(_("Car Detail Link"), max_length=700, blank=True, null=True, unique=True) 
    car_vin = CharField(_("Car VIN"), max_length=200, blank=True, null=True, unique=True) 
    car_stock = CharField(_("Car Stock Type"), max_length=25, blank=True, null=True, choices=CAR_STOCK, default="used", unique=False)
    dealer = ForeignKey(User, on_delete=SET_NULL, related_name='car', null=True)
    car_year = IntegerField(_("Car Manufacturing Year"), blank=True, null=True, choices=CAR_YEAR, default=2000, unique=False)
    car_mileage = DecimalField(_("Car Mileage"), max_digits=40, blank=True, decimal_places=1, null=True, unique=False) 
    car_price = DecimalField(_("Car Main Price"), max_digits=40, blank=True, decimal_places=1, null=True, unique=False)
    car_sub_price = DecimalField(_("Car Old Price"), max_digits=40, blank=True, decimal_places=1, null=True, unique=False)
    videos = FileField(
        _("Upload Car Video"),
        upload_to=car_vid_path,
        null=True,
        blank=True,
    )
    car_map_location = URLField(_("Paste your Google Location"), blank=True, null=True)
    car_door = CharField(_("Car Door"), max_length=15, blank=True, null=True, choices=CAR_DOOR, default="2")
    car_body = CharField(_("Car Body"), max_length=15, blank=True, null=True, choices=CAR_BODY, default="sedan")
    car_history = URLField(_("Car History Link"), max_length=700, blank=True, null=True, unique=True) 
    car_dealer_name = CharField(_("Car Dealer"), max_length=700, blank=True, default="car dealer name", null=True) 
    car_dealer_phone = CharField(_("Car Dealer Phone Number"), max_length=16, blank=True, default="+1864756473547", null=True) 
    car_transmission = CharField(_("Car Transmission"), max_length=50, blank=True, null=True) 
    car_ext_color = CharField(_("Car Ext Color"), max_length=50, blank=True, null=True) 
    car_int_color = CharField(_("Car Int Color"), max_length=50, blank=True, null=True) 
    car_drive_train = CharField(_("Car Drive Train"), max_length=50, blank=True, null=True) 
    car_fuel_type = CharField(_("Car Fuel Type"), max_length=50, blank=True, null=True) 
    car_engine = CharField(_("Car Engine"), max_length=50, blank=True, null=True) 
    likes = ManyToManyField(User, blank=True, related_name="car_likes")
    seller_note = HTMLField(_("Seller Note"), null=True, blank=True, default="From https://cars.com, follow the link to see their reviews and comments on this car")
    status = CharField(_("Status"), max_length=15, blank=True, null=True, choices=STATUS, default=PUBLISHED)
    featured = BooleanField(_('Featured Cars'), default=False)
    special = BooleanField(_('Special Offer'), default=False)
    available = BooleanField(_('Car Availability'), default=True)
    objects = CarManager()

    def __str__(self):
        return self.title

    @property
    def get_related_cars_by_dealer(self):
        return AutoSearch.objects.filter(dealer=self.dealer).order_by("-car_year").exclude(id=self.id)[:3]


    def like_counts(self):
        return self.likes.count()

    @property
    def get_image_url(self):
        img = self.image_set.first()
        if img:
            return img.img_url
        return img #None


    class Meta:
        db_table = 'cars'
        managed = True
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        ordering = ["-created", "-modified", "-car_year"]

    def get_absolute_url(self):
        """Get url for car's detail view.

        Returns:
            str: URL for car detail.

        """
        return reverse("cars:detail", kwargs={"slug": self.slug})


    def get_update_url(self):
        return f"{self.get_absolute_url}/update"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"


class Image(TimeStampedModel):
    car = ForeignKey(AutoSearch, on_delete=CASCADE)
    img_url = URLField(_("Alternative Image Upload Field"), null=True, blank=True, unique=False)
    image = ImageField(
        _("Upload Car Image"), upload_to=post_image, null=True, blank=True
    )

    def __str__(self):
        return f"{self.car.title} photo"

    def get_remote_image(self):
        if self.img_url and self.image:
            result = request.urlretrieve(self.img_url)
            self.image.save(
                os.path.basename(self.img_url),
                File(open(result[0], 'rb'))
                )

    def save(self, *args, **kwargs):
        self.get_remote_image()
        super().save(*args, **kwargs)


    class Meta:
        managed = True
        verbose_name = "Car Files"
        verbose_name_plural = "Car Files"
        ordering = ["-created"]




class WatchCars(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name="userwatch")
    car = ForeignKey(AutoSearch, on_delete=CASCADE, related_name="watchedcar")
    active = BooleanField(default=False)

    def __str__(self):
        return f"{self.car.title} searched by {self.user.fullname}"


    def expired_watch(self):
        now = timezone.now()
        exp_range = self.created + timedelta(days=90)
        if self.created and exp_range > now and self.active:
            return True
        return False

    def expired(self):
        qs = WatchCars.objects.filter(user=self.user, car=self.car, active=True)
        if self.expired_watch:
            qs.delete()
            return True
        return False


    def send_price_change_mail(self):
        if self.car.car_sub_price > 0 and self.user.car_price_notif:
            send_email = send_mail(
                f"Watched Car - {self.car.title} Price change",
                f"There has been a chnage to {self.car.title} price you are watching, \n Please check your watch list to confirm.",
                "notif@autobuyfast.com",
                [self.user.email],
                fail_silently=False
            )
            return send_email
        return False

    def send_sold_change_mail(self):
        if not self.car.available and self.user.car_sold_notif:
            send_email = send_mail(
                f"Watched Car - {self.car.title} Sold",
                f"This vehicle {self.car.title} has been sold, \n Please check your watch list to confirm.",
                "notif@autobuyfast.com",
                [self.user.email],
                fail_silently=False
            )
            return send_email
        return False

    class Meta:
        managed = True
        verbose_name = "Car Watch"
        verbose_name_plural = "Car Watch"
        ordering = ["-created"]


class CarCompare(TimeStampedModel):
    car_one = ForeignKey(AutoSearch, on_delete=SET_NULL, default=4, null=True, related_name="carone")
    car_two = ForeignKey(AutoSearch, on_delete=SET_NULL, default=9, null=True, related_name="cartwo")
    car_three = ForeignKey(AutoSearch, on_delete=SET_NULL, default=3, null=True, related_name="carthree")
    slug = SlugField(max_length=800, blank=True, null=True, unique=True, default="result")
    class Meta:
        managed = True
        verbose_name = "Car Compare"
        verbose_name_plural = "Cars Compared"
        ordering = ["-created"]

class SaveCarSearch(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name="savecarsearch")
    search_link = URLField(blank=True, null=True)
    saved = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.fullname} saved this link {self.search_link}"

    class Meta:
        managed = True
        verbose_name = "Cat Search"
        verbose_name_plural = "Car Searches"
        ordering = ["-created"]
    