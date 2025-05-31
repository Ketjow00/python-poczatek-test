print("To kalkulator średniej predkości twojego biegu.")
import average_speed

distance = int(input("Podaj ile km przebiegłeś/-łaś."))
time = int(input("Podaj przez ile czasu biegłeś/-łaś w godzinach."))

print(f"Twoja średnia prędkość to: {average_speed.average_running_speed(distance, time)} km/h.")