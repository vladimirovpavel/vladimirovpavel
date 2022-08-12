from django.db import models

# Create your models here.

class Trainer (models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.IntegerField()

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.IntegerField()
    phone = models.IntegerField()

class WorkoutPlaces(models.Model):
    name = models.CharField(max_length=50)

class WorkoutType(models.Model):
    workout_type = models.TextChoices("Workout type", "stong_body stretching massage")

class Workouts(models.Model):
    datetime = models.DateTimeField()
    capacity = models.IntegerField(default=3)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
    workout_place_id = models.ForeignKey(WorkoutPlaces, on_delete=models.DO_NOTHING)
    type_type_id = models.ForeignKey(WorkoutType, on_delete=models.DO_NOTHING, default=0)
    

class AthletesOnTrain(models.Model):
    athlete_id = models.ForeignKey(Athlete, on_delete=models.DO_NOTHING)
    workout_id = models.ForeignKey(Workouts, on_delete=models.CASCADE)


# вместимость - у тренировки, ли типа? или площадки?
