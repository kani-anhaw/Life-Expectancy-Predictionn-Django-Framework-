from django.shortcuts import render
from .models import Immunization, Economic, Mortality, Social, Health
import joblib

filename = 'C:/Users/felom/Python/ITD105/ML model/lin_reg.aiml'
model = joblib.load(filename)
def text_lowercase(text):
 return text.lower()

def classifyDiabetes(request):

 immunization_data = Immunization.objects.latest('id')
 g = immunization_data.g
 h = immunization_data.h
 k = immunization_data.k
 m = immunization_data.m

 economic_data = Economic.objects.latest('id')
 b = economic_data.b
 f = economic_data.f
 l = economic_data.l
 o = economic_data.o
 s = economic_data.s

 mortality_data = Mortality.objects.latest('id')
 c = mortality_data.c
 d = mortality_data.d
 e = mortality_data.e
 j = mortality_data.j
 n = mortality_data.n

 health_data = Health.objects.latest('id')
 i = health_data.i
 q = health_data.q
 r = health_data.r

 social_data = Social.objects.latest('id')
 p = social_data.p
 t = social_data.t
 u = social_data.u



 country = ["Afghanistan", "Albania", "Algeria", "Angola", "Antigua and Barbuda",
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
            "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
            "Bhutan", "Bolivia (Plurinational State of)", "Bosnia and Herzegovina", "Botswana",
            "Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "CÃ´te d'Ivoire",
            "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile",
            "China", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Croatia", "Cuba",
            "Cyprus", "Czechia", "Democratic People's Republic of Korea", "Democratic Republic of the Congo",
            "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
            "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",  "Germany",
            "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
            "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
            "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic",
            "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Lithuania", "Luxembourg", "Madagascar","Malawi", "Malaysia",
            "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",  "Mexico",  "Micronesia (Federated States of)",
            "Monaco", "Mongolia", "Montenegro", "Morocco","Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
            "Nicaragua", "Niger", "Nigeria", "Niue", "Norway", "Oman", "Pakistan", "Palau","Panama", "Papua New Guinea", "Paraguay", "Peru",
            "Philippines", "Poland", "Portugal", "Qatar", "Republic of Korea", "Republic of Moldova", "Romania",  "Russian Federation", "Rwanda",
            "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
            "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
            "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Tajikistan",
            "Thailand", "The former Yugoslav republic of Macedonia", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
            "Turkmenistan", "Tuvalu", "Uganda",  "Ukraine", "United Arab Emirates", "United Kingdom of Great Britain and Northern Ireland", "United Republic of Tanzania",
            "United States of America", "Uruguaay", "Uzbekistan", "Vanuatu", "Venezuela (Bolivarian Republic of)",  "Viet Nam", "Yemen", "Zambia", "Zimbabwe"]

 v=0
 for i, element in enumerate(country):
  if element == u:
   v = i



 sampletest = [[v, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]]
 predicted = model.predict(sampletest)
 predicted = round(predicted[0])

 return render(request, 'app/immunization.html', {"result2":predicted})

