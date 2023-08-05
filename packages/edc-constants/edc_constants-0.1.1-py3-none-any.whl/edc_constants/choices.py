from django.utils.translation import ugettext_lazy as _

from .constants import NOT_APPLICABLE, YES, NO, ALIVE, DEAD, UNKNOWN

# choices
BLANK_CHOICE_DASH = [('', '---------')]

""" Try to keep this in alphabetical order """

ACU_EST = (
    ('Acute', 'Acute'),
    ('Established', 'Established'),
)
PIMA = (
    ('Participant Declined', 'Participant Declined'),
    ('Multiple PIMA malfunction', 'Multiple PIMA malfunction'),
    ('Failed Blood Collection', 'Failed Blood Collection'),
    ('OTHER', _('Other, specify:')),
)

ACU_EST_NEG = (
    ('Acute', 'Acute'),
    ('Established', 'Established'),
    ('Negative', 'Negative'),
)

ALIVE_DEAD = (
    (ALIVE, 'Alive'),
    (DEAD, 'Dead'),
)

ALIVE_DEAD_UNKNOWN = (
    (ALIVE, 'Alive'),
    (DEAD, 'Dead'),
    (UNKNOWN, 'Unknown'),
)

ART_STATUS = (
    ('ON', 'Yes, ON ART'),
    ('STOPPED', 'No, stopped ART'),
    ('NAIVE', 'No, have never taken ART'),
)

ART_STATUS_UNKNOWN = (
    ('ON', 'ON ART'),
    ('STOPPED', 'Stopped'),
    ('NAIVE', 'Naive'),
    ('UNKNOWN', 'Unknown'),

)

ART_STATUS_CONFIRM = (
    ('OPD', '1. Show OPD/IDCC card'),
    ('Pills', '2. Show Pills'),
    ('Pic', '3. Identify Pictorial'),
)

CONFIRMED_SUSPECTED = (
    ('CONFIRMED', 'Confirmed'),
    ('SUSPECTED', 'Suspected'),
)

COUNTRY = (
    ('botswana', 'Botswana'),
    ('zimbabwe', 'Zimbabwe'),
    ('rsa', 'South Africa'),
    ('zambia', 'Zambia'),
    ('namibia', 'Namibia'),
    ('nigeria', 'Nigeria'),
    ('china', 'China'),
    ('india', 'India'),
    ('OTHER', 'Other'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('AnyDay', 'Any Day'),
)

TIME_OF_DAY = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
    ('Anytime', 'Anytime'),
)


DATE_ESTIMATED = (
    ('-', 'No'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)

DEATH_RELATIONSIP_TO_STUDY = (
    ('Definitely not related', 'Definitely not related'),
    ('Probably not related', 'Probably not related'),
    ('Possible related', 'Possible related'),
    ('Probably related', 'Probably related'),
    ('Definitely related', 'Definitely related')
)

DRUG_FORMULATION = (
    ('11', 'Tablet'),
    ('12', 'Capsule'),
    ('13', 'Liquid'),
    ('14', 'Powder'),
    ('15', 'Suspension'),
    ('16', 'Gel'),
    ('17', 'Oil'),
    ('18', 'Lotion'),
    ('19', 'Cream'),
    ('20', 'Patch'),
    ('99', 'Other'),
)

DRUG_ROUTE = (
    ('1', 'Intramuscular'),
    ('2', 'Intravenous'),
    ('3', 'Oral'),
    ('4', 'Topical'),
    ('5', 'Subcutaneous'),
    ('6', 'Intravaginal'),
    ('7', 'Rectal'),
    ('9', 'Other'),
)

FEEDING = (
    ('BF', 'Breast Feed'),
    ('FF', 'Formula Feed'),
)

GENDER = (
    ('M', _('Male')),
    ('F', _('Female')),
)

GENDER_UNDETERMINED = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('U', _('Undetermined')),
)

"""do not change without inspecting implication to check_omang_field() in utils.py"""
IDENTITY_TYPE = (
    ('OMANG', 'Omang'),
    ('DRIVERS', 'Driver\'s License'),
    ('PASSPORT', 'Passport'),
    ('OMANG_RCPT', 'Omang Receipt'),
    ('OTHER', 'Other'),
)


NORMAL_ABNORMAL = (
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
)

NORMAL_ABNORMAL_NOEXAM = (
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
    ('NO_EXAM', 'No Exam Performed'),
)

NORMAL_ABNORMAL_NOTEVALUATED = (
    ('NORMAL', 'Normal'),
    ('ABNORMAL', 'Abnormal'),
    ('NOT_EVAL', 'Not Evaluated'),
)

POS_NEG = (
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('IND', 'Indeterminate'),
)

POS_NEG_REFUSED = (
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('IND', 'Indeterminate'),
    ('REF', 'Refused to disclose'),
)

POS_NEG_ANY = (
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('ANY', 'Any'),
)

POS_NEG_ONLY = (
    ('POS', _('Positive')),
    ('NEG', _('Negative')),
)

POS_NEG_UNKNOWN = (
    ('POS', _('Positive')),
    ('NEG', _('Negative')),
    ('UNKNOWN', _('Unknown')),
)

POS_NEG_ACU = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative'),
    ('Possible Acute', 'Possible Acute'),
    ('Indeterminate', 'Indeterminate'),
)

POS_NEG_NOTESTED = (
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('NEVER', 'Never tested for HIV'),
)


POS_NEG_UNTESTED_REFUSAL = (
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('NEVER', 'Never tested for HIV'),
    ('UNK', 'Unknown'),
    ('REFUSED', 'Refused to answer'),
)

REFUSAL_STATUS = (
    ('REFUSED', 'Refused'),
    ('NOT_REFUSED', 'No longer refusing'),
)

SEVERITY_LEVEL = (
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
)

SEXUAL_DEBUT = (
    ('<=14', '14 or under'),
    ('15-17', ' 15 - 17'),
    ('>=18', '18 or above'),
)

TIME_OF_WEEK = (
    ('weekdays', 'Weekdays'),
    ('weekend', 'Weekends'),
)

TIME_OF_DAY = (
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
)

TIME_UNITS = (
    ('TODAY', 'Today'),
    ('DAYS', 'Days'),
    ('WEEKS', 'Weeks'),
    ('MONTHS', 'Months'),
    ('YEARS', 'Years'),
)

URINALYSIS = (
    ('NAD', 'NAD'),
    ('Sugar Neg', 'Sugar Neg'),
    ('Sugar +', 'Sugar +'),
    ('Sugar ++', 'Sugar ++'),
    ('Sugar +++', 'Sugar +++'),
    ('Blood', 'Blood'),
    ('Protein', 'Protein'),
    ('Cells', 'Cells'),
)

WILL_DECL = (
    ('WILLING', 'Willing'),
    ('DELINED', 'Declined'),
)

YES_NO = (
    (YES, _(YES)),
    (NO, _(NO)),
)

YES_NO_DECLINED = (
    (YES, YES),
    (NO, NO),
    ('Declined', 'Yes, but subject declined copy'),
)

YES_NO_OPTIONAL = (
    (YES, YES),
    (NO, NO),
    ('Optional', 'Optional'),
)

YES_NO_REFUSED = (
    (YES, _(YES)),
    (NO, _(NO)),
    ('REF', _('Refused to answer')),
)

YES_NO_DWTA = (
    (YES, _(YES)),
    (NO, _(NO)),
    ('DWTA', _('Don\'t want to answer')),
)

YES_NO_NA_SPECIFY = (
    (YES, 'Yes, (Specify below)'),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NA = (
    (YES, YES),
    (NO, NO),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NOT_EVALUATED = (
    (YES, YES),
    (NO, NO),
    ('Not_evaluated', 'Not evaluated'),
)

YES_NO_NOT_EVALUATED_NA = (
    (YES, YES),
    (NO, NO),
    ('Not_evaluated', 'Not evaluated'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_NOT_DONE = (
    (YES, YES),
    (NO, NO),
    ('Not_done', 'Not Done'),
)

YES_NO_DOESNT_WORK = (
    (YES, YES),
    (NO, NO),
    ('DontWork', 'Doesn\'t work'),
)

YES_NO_UNKNOWN = (
    (YES, YES),
    (NO, NO),
    ('Unknown', 'Unknown'),
)

YES_NO_UNKNOWN_NA = (
    (YES, YES),
    (NO, NO),
    ('Unknown', 'Unknown'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_UNSURE = (
    (YES, YES),
    (NO, NO),
    ('Not Sure', 'Not Sure'),
)

YES_NO_UNSURE_NA = (
    (YES, YES),
    (NO, NO),
    ('Not Sure', 'Not Sure'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

YES_NO_DONT_KNOW = (
    (YES, YES),
    (NO, NO),
    ('Dont_know', 'Do not Know'),
)

YES_NO_DONT_KNOW_NA = (
    (YES, YES),
    (NO, NO),
    ('Dont_know', 'Do not Know'),
    (NOT_APPLICABLE, 'Not applicable'),
)

YES_NO_DOESNT_WORK = (
    (YES, YES),
    (NO, NO),
    ('Doesnt_work', 'Doesnt Work'),
)
