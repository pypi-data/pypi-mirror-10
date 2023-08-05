# oppia/awards.py

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, F
from django.utils import timezone

from oppia.models import Badge, Award, AwardCourse
from oppia.models import Tracker, Course, Section, Activity, Media
from oppia.quiz.models import Quiz, QuizAttempt, QuizProps
from oppia.signals import badgeaward_callback

models.signals.post_save.connect(badgeaward_callback, sender=Award)

def courses_completed(hours):
    try:
        badge = Badge.objects.get(ref='coursecompleted')
    except Badge.DoesNotExist:
        print "Badge not found: coursecompleted"
        return
    
    print hours
    # create batch of course with all the digests for each course
    courses = Course.objects.filter(is_draft=False, is_archived=False)
    for c in courses:
        digests = Activity.objects.filter(section__course=c).values('digest').distinct()
            
        # get all the users who've added tracker for this course in last 'hours'
        if hours == 0:
            users = User.objects.filter(tracker__course=c).distinct()
            
        else:
            since = timezone.now() - datetime.timedelta(hours=int(hours))
            users = User.objects.filter(tracker__course=c, tracker__submitted_date__gte=since).distinct()
       
        for u in users:            
            user_completed = Tracker.objects.filter(user=u, course=c, completed=True, digest__in=digests).values('digest').distinct().count()
            if digests.count() == user_completed and AwardCourse.objects.filter(award__user=u,course=c).count() == 0:
                print c.title
                print "-----------------------------"
                print digests.count()
                print u.username + " AWARD BADGE"
                award = Award()
                award.badge = badge
                award.user = u
                award.description = "Course completed: " + c.get_title()
                award.save()
                
                am = AwardCourse()
                am.course = c
                am.award = award
                am.course_version = c.version
                am.save()
    
    return
