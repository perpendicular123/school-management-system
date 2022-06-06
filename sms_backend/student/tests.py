from django.test import TestCase
from student.models import user_model

# Create your tests here.

class RegisterStudentTestCases(TestCase):
    def setup(self):
        student_payload ={   
        "name":"ritiyuik",
        "surname":"mnjikk",
        "email":"23uisd24s3weri@gmail.com",
        "address":"fsfsd",
        "role":"student",
        "password":"tassdsf2sfds90se234sf23344y34227gfs3"
        },    

        parents_payload ={
        "name":"ristiudfjdfisdk",
        "surname":"mnjsfijsdjfsdjfkk",
        "email":"sfvs33dsfss322fsfsde3aszdadesurt5fs24dfii@gmail.com",
        "address":"f45sfe3sdffsd",
        "role":"parent",
        "password":"opsdfs5stfss45dfds4saf342wr4fsffty"
        },
        student = user_model.objects.bulk_create([student_payload,])
        
    def test_for_student_register(self):

