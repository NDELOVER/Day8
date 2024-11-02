def calculate_love_score(name1, name2):
    combined_name=(name1+name2).lower()
    ti = 0
    ri = 0
    ui = 0
    ei = 0
    for t in combined_name:
        if t == "t":
            ti += 1
    for r in combined_name:
        if r == "r":
            ri += 1
    for u in combined_name:
        if u == "u":
            ui += 1
    for e in combined_name:
        if e == "e":
            ei += 1
    print(f"T occurs {ti} times")
    print(f"R occurs {ri} times")
    print(f"U occurs {ui} times")
    print(f"E occurs {ei} times")
    total_name = ti + ri + ui + ei
    print(f"Total={total_name}")
    li = 0
    oi = 0
    vi = 0
    eii = 0
    for l in combined_name:
        if l == "l":
            li += 1
    for o in combined_name:
        if o == "o":
            oi += 1
    for v in combined_name:
        if v == "v":
            vi += 1
    for e in combined_name:
        if e == "e":
            eii += 1
    print(f"L occurs {li} times")
    print(f"O occurs {oi} times")
    print(f"V occurs {vi} times")
    print(f"E occurs {eii} times")
    total_love = li+oi+vi+eii
    print(f"Total={total_love}")
    print(f"Love Score = {total_name}{total_love}" )
calculate_love_score("Kanye West", "Kim Kardashian")


