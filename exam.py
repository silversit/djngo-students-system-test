
terrains = {
    "mountain": -10.0,
    "desert": -15.0,
    "forest": 7.0
}
iniitial_energy = float(input())
counter = 0
artifact = 0
end_command = "Journey ends here!"
ending = False
outcome = ""
while True:
    terarain = input()
    if terarain != end_command:
        iniitial_energy += terrains[terarain]

    if terarain == end_command:
        ending= True
        break
    if terarain == "mountain":
        counter +=1
        if counter % 3 == 0:
            artifact +=1
            counter =0
    if artifact == 3:
        outcome = f'The character reached the legendary artifact with {format(iniitial_energy, ".2f")} energy left.'

        break
    elif iniitial_energy <=0:
        outcome = "The character is too exhausted to carry on with the journey."
        break



if artifact <3 and  ending:
    outcome = f'The character could not find all the pieces and needs {abs(artifact - 3)} more to complete the legendary artifact.'

print(outcome)




