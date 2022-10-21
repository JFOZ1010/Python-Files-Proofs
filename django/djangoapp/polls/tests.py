from asyncio import futures
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


from .models import Question

def create_choice(pk, choice_text, votes=0):
    """
        Create a choice that have the pk(primary key is a number) of a specific question
        with the given "choice_text" and with the given "votes"(votes starts in zero)
    """
    question = Question.objects.get(pk=pk)
    return question.choice_set.cr(choice_text=choice_text, votes=votes)

# Create your tests here.
class QuestionModelTests(TestCase):

    """
    def setUp(self):
        self.question = Question.objects.create(question_text="¿Qué es Django?")
    """


    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently() returns `False` for questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30) #30 dias en el futuro
        #future_question = Question(question_text="¿Quien es el Mejor Profe de programación de platzi?", pub_date=time)
        #self.question.pub_date = time
        future_question = Question(question_text="¿pregunta del futuro :D?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) #comprueba que la pregunta no se haya publicado recientemente

    #esta test de funcion, comprueba que la fecha de publicación sea menor o igual a la fecha actual
    def test_was_published_recently_with_past_questions(self):
        """
        was_published_recently() returns `False` for questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(hours=24) #1 dia y 1 segundo en el pasado
        #self.question.pub_date = time
        past_question = Question(question_text="¿pregunta del pasado :D?", pub_date=time)
        self.assertIs(past_question.was_published_recently(), False) #comprueba que la pregunta no se haya publicado recientemente

    def test_was_published_recently_with_present_questions(self):
        """
        was_published_recently() returns `True` for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        #self.question.pub_date = time
        present_question = Question(question_text="¿pregunta del presente :D?", pub_date=time)
        self.assertIs(present_question.was_published_recently(), True) #comprueba que la pregunta se haya publicado recientemente

    def create_question(question_text, days): 
        """
            Create a question with the given `question_text` and published the given number of `days` offset to now (negative for questions published in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)
    
#este test de view, se encarga de, cuando se haga una petición a la url de la vista index, se comprueba que se muestre la vista index, y que se muestren las preguntas que se hayan creado pero que no se hayan publicado y además que no se muestren las preguntas que se hayan publicado que sean más de 1 día en el futuro, y que se muestren las preguntas que se hayan publicado y que sean menos de 1 día en el presente.
class QuestionIndexViewTests(TestCase):

    def test_question_without_choices(self):
        """
        Quetions have no choices aren't displayed in the index view
        """
        question = create_question("Cuál es tu curso favorito?", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_question_with_choices(self):
        """
        Question with choices are displayed in the index view
        """
        question = create_question("Cuál es tu curso favorito?", days=-10)
        choice1 = create_choice(pk=question.id, choice_text="Curso Básico de Django", votes=0)
        choice2 = create_choice(pk=question.id, choice_text="Curso de Introducción a la Nube con Azure", votes=0)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])


    def create_question(self, question_text, days):
        """
        Create a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        self.create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page.
        """
        question = self.create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question] #comprueba que la pregunta que se haya creado en el pasado, se muestre en la vista index
        )

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions, are displayed.
        """
        past_question = self.create_question(question_text="Past question.", days=-30)
        future_question = self.create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_question]) #comprueba que la pregunta que se haya creado en el pasado, se muestre en la vista index, pero la del futuro no



    def test_two_past_question(self):
        """
        The questions index page may display multiple questions.
        """
        past_question1 = self.create_question(question_text="Past question 1.", days=-30)
        past_question2 = self.create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_question2, past_question1]) #comprueba que las preguntas que se hayan creado en el pasado, se muestren en la vista index
    
    def test_two_future_question(self):
        """
        The questions index will not displayed the questions in the future.
        """
        future_question1 = self.create_question(question_text="Future question 1.", days=50)
        future_question2 = self.create_question(question_text="Future question 2.", days=60)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

class QuestionDetailViewTests(TestCase): 

    def create_question(self, question_text, days):
        """
        Create a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

    def test_future_question(self): 
        """
        the detail view of a question with a pub date in the future returns a 404 not found. 
        """
        future_question = self.create_question(question_text="Future question.", days=50)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404) #

    def test_past_question(self):
        """
        the detail view of a question with a pub date in the past displayed the question`s text. 
        """
        past_question = self.create_question(question_text="Past question.", days=-50)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionResultViewTests(TestCase):
    
        def create_question(self, question_text, days):
            """
            Create a question with the given `question_text` and published the
            given number of `days` offset to now (negative for questions published
            in the past, positive for questions that have yet to be published).
            """
            time = timezone.now() + datetime.timedelta(days=days)
            return Question.objects.create(question_text=question_text, pub_date=time)
    
        def test_future_question(self):
            """
            the result view of a question with a pub date in the future returns a 404 not found.
            """
            future_question = self.create_question(question_text="Future question.", days=50)
            url = reverse("polls:results", args=(future_question.id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)
    
        def test_past_question(self):
            """
            the result view of a question with a pub date in the past displayed the question`s text.
            """
            past_question = self.create_question(question_text="Past question.", days=-50)
            url = reverse("polls:results", args=(past_question.id,))
            response = self.client.get(url)
            self.assertContains(response, past_question.question_text)
    
