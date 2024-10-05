import pandas as pd
import streamlit as st
import generate_combinations

costs = pd.DataFrame([
    ["R",       "weak",     30,     39],
    ["",        "strong",   45,     60],
    ["SR",      "weak",     75,     102],
    ["",        "strong",   105,    141],
    ["SSR",     "",         150,    204],
    ["support", "",         96,     126]
    ], columns=["rarity", "power", "-", "+"])

r_weak_cards = "R weak: 軽い足取り、愛嬌、準備運動、ファンサ、バランス感覚、今日もおはよう、ゆるふわおしゃべり、もう少しだけ、リスタート、えいえいおー、リズミカル  \n"
sr_weak_cards = "SR weak: 決めポーズ、アドリブ、情熱ターン、眼力、大声援、ラブリーウインク、ありがとうの言葉、あふれる思い出、ふれあい"

lower_limits = ["306 (B, B+)", "441 (A, A+)", "546 (S, S+)"]
upper_limits = ["363 (B)", "423 (B+)", "519 (A)", "594 (A+)", "642 (S)", "741 (S+)"]

def main():
    st.title("Combination Generator")
    st.dataframe(costs, hide_index=True)
    skill_cards = st.text_input("skill cards", placeholder="204,204,141,60,45,39,30 (input comma-delimited card costs.)",
        help=(r_weak_cards + sr_weak_cards))
    requirement_cards = st.text_input("requirement cards", placeholder="0,1 (input indexes of required skill cards.)")
    lower_limit = st.selectbox("lower limit", lower_limits, index=2)
    upper_limit = st.selectbox("upper limit", upper_limits, index=4)

    ok = st.button("OK")
    if ok:
        skill_cards = list(map(int, skill_cards.split(",")))
        skill_cards_dict = {}
        for i, skill_card in enumerate(skill_cards):
            skill_cards_dict[i] = skill_card

        df = generate_combinations.generate_combinations(
            skill_cards_dict,
            list(map(int, requirement_cards.split(","))),
            int(lower_limit.split()[0]),
            int(upper_limit.split()[0])
        )

        numerator = len(df[df["requirement"] == True])
        denominator = len(df)

        st.text(f"{(numerator / denominator) :.1%} ({numerator}/{denominator})")
        st.dataframe(df, hide_index=True)

if __name__ == "__main__":
    main()