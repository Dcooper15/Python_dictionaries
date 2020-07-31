ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit['email'])
ramitinterest = ramit["interests"][0]
print(ramitinterest)

jasmine_email = ramit['friends'][0]['email']
print(jasmine_email)

jan_interest = ramit['friends'][1]['interests'][1]
print(jan_interest)