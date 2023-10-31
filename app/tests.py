from django.test import SimpleTestCase

# Create your tests here.
class test_near_hundred(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get("/warmup-1/near-hundred/93")
        self.assertContains(response, True)
    def test_near_hundred_90(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, True)
    def test_near_hundred_89(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, False)

class test_String_Splosion(SimpleTestCase):
    def test_String_Splosion_Code(self):
        response = self.client.get("/warmup-2/String-Splosion/Code")
        self.assertContains(response, "CCoCodCode")
    def test_String_Splosion_Code_abc(self):
        response = self.client.get("/warmup-2/String-Splosion/abc")
        self.assertContains(response, "aababc")
    def test_String_Splosion_Code_ab(self):
        response = self.client.get("/warmup-2/String-Splosion/ab")
        self.assertContains(response, "aab")

class test_cat_dog(SimpleTestCase):
    def test_cat_dog_One_TRUE(self):
        response = self.client.get("/String-2/cat-dog/catdog")
        self.assertContains(response, True)
    def test_cat_dog_One_FALSE(self):
        response = self.client.get("/String-2/cat-dog/catcat")
        self.assertContains(response, False)
    def test_cat_dog_Two_TRUE(self):
        response = self.client.get("/String-2/cat-dog/1cat1cadodog")
        self.assertContains(response, True)

class test_lone_sum(SimpleTestCase):
    def test_lone_sum_6(self):
        response = self.client.get("/Logic-2/lone-sum/1/2/3")
        self.assertContains(response, 6)
    def test_lone_sum_2(self):
        response = self.client.get("/Logic-2/lone-sum/3/2/3")
        self.assertContains(response, 2)
    def test_lone_sum_0(self):
        response = self.client.get("/Logic-2/lone-sum/3/3/3")
        self.assertContains(response, 0)