from js import document

def signup(event):
    grade = document.getElementById("grade_level").value
    section = document.getElementById("team").value  # this is SECTION

    if grade == "" or section == "":
        document.getElementById("output").innerHTML = " Please complete all fields."
        return

    grade = int(grade)
    section = section.upper()

    team = ""

    # ===== GRADE 7 =====
    if grade == 7 and section == "RUBY":
        team = "Yellow Tigers"
    elif grade == 7 and section == "SAPPHIRE":
        team = "Red Bulldogs"
    elif grade == 7 and section == "EMERALD":
        team = "Blue Bears"
    elif grade == 7 and section == "TOPAZ":
        team = "Green Hornets"

    # ===== GRADE 8 =====
    elif grade == 8 and section == "EMERALD":
        team = " Yellow Tigers"
    elif grade == 8 and section == "RUBY":
        team = "Red Bulldogs"
    elif grade == 8 and section == "TOPAZ":
        team = "Blue Bears"
    elif grade == 8 and section == "JADE":
        team = "Blue Bears"
    elif grade == 8 and section == "SAPPHIRE":
        team = "Green Hornets"

    # ===== GRADE 9 =====
    elif grade == 9 and section == "SAPPHIRE":
        team = "Yellow Tigers"
    elif grade == 9 and section == "TOPAZ":
        team = "Red Bulldogs"
    elif grade == 9 and section == "RUBY":
        team = "Blue Bears"
    elif grade == 9 and section == "JADE":
        team = "Green Hornets"
    elif grade == 9 and section == "EMERALD":
        team = "Green Hornets"

    # ===== GRADE 10 =====
    elif grade == 10 and section == "SAPPHIRE":
        team = "Yellow Tigers"
    elif grade == 10 and section == "EMERALD":
        team = " Red Bulldogs"
    elif grade == 10 and section == "TOPAZ":
        team = " Blue Bears"
    elif grade == 10 and section == "RUBY":
        team = "Green Hornets"

    

    else:
        team = " No intrams team assigned."

  document.getElementById("signupBtn").addEventListener("click", signup)
    