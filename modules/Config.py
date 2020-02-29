
def createTheme(prim, sec):
    theme =  {
        "Primary": prim,
        "Secondary": sec["default"],
        "Menu" : [prim["game"][0], sec["default"][0], sec["default"][1], prim["font"][0]]
    }
    theme["Primary"]["notification"] = sec["notification"]
    return theme

darkTheme = {
    "interface": "#141417",
    "background": "#343444",

    "game": ["#25242e", "#aeabc7"],
    "font": ["#aeabc7", "#25242e"],

    "warning": "#AA3233",

}

lightTheme = {
    "interface": "#9592b4",
    "background": "#f2f2ff",

    "game": ["#c6c3e4", "#666474"],
    "font": ["#25242e", "#f2f2ff"],

    "warning": "#ec9462"
}

themes = {
    "Primary": {
        "Day": lightTheme,
        "Night": darkTheme
    },
    "Secondary": {
        "Gold" : {
            "default": ["#444433", "#998755"],
            "notification": ["#cba36e"]
        },
        "Beach" : {
            "default": ["#2e998f", "#b4a066"],
            "notification": ["#35baae"]
        },
        "Cyan" : {
            "default": ["#44cbbf", "#a2dbe6"],
            "notification": ["#35baae"]
        },
    }
}
