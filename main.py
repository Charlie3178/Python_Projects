ttl = input("Please enter the text for the heading: ")
hdng_tpe = input("Please enter the size of the heading (1 - 6): ")


def heading_gen(title,heading_type):
   return f'<h{heading_type}>{title}</h{heading_type}>'
    

print(heading_gen(ttl,hdng_tpe))