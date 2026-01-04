from random import randrange

_TIPS = [
    "Dammsug sängar.",
    "Damma tavlor och lampor.",
    "Städa under diskbänken.",
    "Ta bort fula fläckar på väggar och andra platser.",
    "Städa och rensa i badrumsskåp.",
    "Gör rent persienner och runt gardiner.",
    "Rengör micron.",
    "Putsa speglar.",
    "Städa golvbrunnarna.",
    "Kontrollera att vattnet rinner i alla avlopp.",
    "Städa i och runt ugnen.",
    "Töm nålfilter och rengör kondenstrumman.",
    "Rensa bland viktiga papper. Lägg in i kalendern vid behov.",
    "Gå igenom frysarna.",
    "Rensa ut gammal teknik.",
    "Putsa mässingsljusstakar.",
    "Gå igenom kryddhyllan.",
    "Städa upp i spat.",
    "Städa i duschen. Torka bort allt vatten vid fönstret.",
    "Rengör ljusknappar och dörrhandtag.",
]


def random_tip() -> str:
    """Returns a random tip from the current list.

    From the beginning the list will contain all available tips and return a
    random one. The next time that tip will be removed and a random one from
    those that remain will be returned and so on until the list is empty. Then
    it will be refilled with all available tips again.

    This function uses a file to remember which tips have already been used so
    this function isn't thread safe.
    """
    TIPS_FILENAME = ".tips"

    all_tips: list[str] = []

    try:
        with open(TIPS_FILENAME, "r", encoding="utf-8") as file:
            all_tips = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # the file needs to be created once
        all_tips = _TIPS.copy()
        with open(TIPS_FILENAME, "w", encoding="utf-8") as file:
            for tip in all_tips:
                file.write(tip + "\n")

    if len(all_tips) == 0:
        all_tips = _TIPS.copy()

    tip_index = randrange(len(all_tips))
    todays_tip = all_tips.pop(tip_index)

    with open(TIPS_FILENAME, "w", encoding="utf-8") as file:
        for tip in all_tips:
            file.write(tip + "\n")

    return todays_tip
