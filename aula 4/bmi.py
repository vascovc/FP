# coding: utf-8

# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.
def bodyMassIndex(height, weight):
    # Complete the function definition...
    bmi = ...
    return bmi


# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 
def bmiCategory(bmi):
    # Complete the function definition...
    ...


# This is the main function
def main():
    print("Índice de Massa Corporal")
    altura = float(input("Altura (m)? "))
    peso = float(input("Peso (kg)? "))

    # Complete the function calls...
    imc = bodyMassIndex(...)
    cat = ...

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)


# Program starts executing here
main()

