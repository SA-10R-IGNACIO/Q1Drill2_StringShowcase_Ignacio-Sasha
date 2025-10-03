from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value
    birthday = document.querySelector("#birthday").value
    food = document.querySelector("#food").value

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f"""👤 Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}
    birthday : {birthday}
    food : {food}

    ✏️ Notes:
    {name} is currently {age} years old and studies at {school}.
    Their birthday is on {birthday}, and their favorite food is {food}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")
