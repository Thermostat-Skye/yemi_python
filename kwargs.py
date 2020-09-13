def list_countries(**kwargs):
    for country, capital in kwargs.items():
        print(f"{capital} is the Capital of {country}")

list_countries(Nigeria='Abuja', Cameroun='Younde', England='London')