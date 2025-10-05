languages = {
    'rob': 'python',
    'rupert': 'c',
    'dave': 'rust',
    'bob': 'python'
}

people_to_check = [  'rob', 'rupert','dave', 'mollie']
for person in people_to_check:
    if person in languages:
        print(f"Thanks for submitting your answer, {person.title()}")
    else:
        print(f"{person.title()}, please submit your response")