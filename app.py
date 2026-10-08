import streamlit as st
from streamlit_ace import st_ace
from ai import analyze_error, explain_code


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="DebugBuddy",
    page_icon="🐞",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% -10%,
            rgba(0, 255, 120, 0.10),
            transparent 35%
        ),
        #06100b;
    color: #e8fff0;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #06100b;
}

::-webkit-scrollbar-thumb {
    background: #168f4d;
    border-radius: 10px;
}

.debugbuddy-title {
    text-align: center;
    font-size: 58px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 5px;
    margin-bottom: 3px;

    background: linear-gradient(
        90deg,
        #48ff91,
        #00d96b,
        #8affb5
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 25px rgba(0, 255, 120, 0.20);
}

.debugbuddy-subtitle {
    text-align: center;
    font-size: 20px;
    color: #b9d9c3;
    margin-bottom: 6px;
}

.debugbuddy-tagline {
    text-align: center;
    font-size: 12px;
    letter-spacing: 5px;
    color: #37d978;
    font-weight: 700;
    margin-bottom: 30px;
}

div[role="radiogroup"] {
    gap: 10px;
}

div[role="radiogroup"] label {
    background: rgba(0, 255, 120, 0.04);
    border: 1px solid rgba(0, 255, 120, 0.15);
    border-radius: 10px;
    padding: 8px 15px;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    color: #e8fff0;
    margin-top: 15px;
    margin-bottom: 10px;
}

.feature-card {
    border: 1px solid rgba(0, 255, 120, 0.16);
    border-radius: 15px;
    padding: 20px;
    text-align: center;

    background:
        linear-gradient(
            145deg,
            rgba(0, 255, 120, 0.07),
            rgba(0, 255, 120, 0.015)
        );

    margin-bottom: 22px;

    transition: all 0.2s ease;
}

.feature-card:hover {
    border-color: rgba(0, 255, 120, 0.45);
    box-shadow: 0 0 25px rgba(0, 255, 120, 0.08);
}

.feature-icon {
    font-size: 28px;
    margin-bottom: 7px;
}

.feature-title {
    font-size: 19px;
    font-weight: 800;
    color: #72ff9f;
    margin-bottom: 5px;
}

.feature-description {
    font-size: 13px;
    color: #a8c5b0;
}

.code-editor-title {
    color: #72ff9f;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 7px;
}

.result-card {
    border: 1px solid rgba(0, 255, 120, 0.15);
    border-radius: 14px;
    padding: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(0, 255, 120, 0.055),
            rgba(0, 255, 120, 0.015)
        );

    margin-top: 8px;
    margin-bottom: 15px;

    color: #d9f4df;
    line-height: 1.65;
}

.stButton > button {
    border-radius: 10px;
    min-height: 46px;

    background:
        linear-gradient(
            135deg,
            #0f8f4b,
            #12b85e
        );

    color: white;

    border: 1px solid #31e878;

    font-weight: 800;

    box-shadow:
        0 0 15px rgba(0, 255, 120, 0.12);

    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #72ff9f;

    box-shadow:
        0 0 25px rgba(0, 255, 120, 0.25);

    transform: translateY(-1px);
}

.stTextArea textarea {
    background: #09150e !important;
    color: #d9f4df !important;

    border: 1px solid #193d28 !important;
    border-radius: 10px !important;

    font-family:
        "Consolas",
        "Cascadia Code",
        "Courier New",
        monospace !important;
}

.stSelectbox > div > div {
    background: #09150e;
    border-color: #193d28;
}

hr {
    border-color: rgba(0, 255, 120, 0.12);
}

.footer {
    text-align: center;
    margin-top: 55px;
    padding-top: 22px;

    border-top:
        1px solid rgba(0, 255, 120, 0.12);

    color: #6d8e76;

    font-size: 13px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

pre {
    border-radius: 12px !important;
    border: 1px solid rgba(0, 255, 120, 0.15) !important;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HERO
# ==================================================

st.markdown(
    '<div class="debugbuddy-title">🐞 DebugBuddy</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="debugbuddy-subtitle">Your AI coding companion</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="debugbuddy-tagline">UNDERSTAND • DEBUG • LEARN</div>',
    unsafe_allow_html=True
)


# ==================================================
# FEATURE SELECTION
# ==================================================

feature = st.radio(
    "Choose what you want to do",
    [
        "🐞 Debug an Error",
        "📚 Explain My Code"
    ],
    horizontal=True
)

st.divider()


# ==================================================
# LANGUAGE
# ==================================================

language = st.selectbox(
    "💻 Programming Language",
    ["Python", "C", "C++", "Java"]
)

st.divider()


# ==================================================
# DEBUG ERROR MODE
# ==================================================

if feature == "🐞 Debug an Error":

    st.markdown(
        '<div class="section-title">🐞 Find and Understand Your Error</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Paste your code and error message. DebugBuddy helps you understand the problem instead of simply giving you the answer."
    )


    # ==================================================
    # LEARNING MODE
    # ==================================================

    mode = st.radio(
        "🎓 Learning Mode",
        ["Learn", "Fix"],
        horizontal=True
    )


    # ==================================================
    # FEATURE CARDS
    # ==================================================

    card1, card2, card3 = st.columns(3)

    with card1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔎</div>
            <div class="feature-title">Detect</div>
            <div class="feature-description">
                Find the type and location of the error.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with card2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Understand</div>
            <div class="feature-description">
                Get simple explanations and progressive hints.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with card3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Learn</div>
            <div class="feature-description">
                Understand the programming concept behind the error.
            </div>
        </div>
        """, unsafe_allow_html=True)


    # ==================================================
    # CODE + ERROR
    # ==================================================

    code_col, error_col = st.columns(2)


    # ==================================================
    # CODE EDITOR
    # ==================================================

    with code_col:

        st.markdown(
            '<div class="section-title">💻 Your Code</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="code-editor-title">● main.py</div>',
            unsafe_allow_html=True
        )

        ace_mode = {
            "Python": "python",
            "C": "c_cpp",
            "C++": "c_cpp",
            "Java": "java"
        }[language]

        code = st_ace(
            value='name = "Asha"\nprint("Hello " + nme)',
            language=ace_mode,
            theme="dracula",
            key="debug_code_editor",
            height=320,
            font_size=15,
            tab_size=4,
            show_gutter=True,
            show_print_margin=False,
            wrap=False,
            auto_update=True
        )


    # ==================================================
    # ERROR INPUT
    # ==================================================

    with error_col:

        st.markdown(
            '<div class="section-title">❌ Error Message</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="code-editor-title">● terminal</div>',
            unsafe_allow_html=True
        )

        error = st.text_area(
            "Error",
            height=320,
            placeholder="NameError: name 'nme' is not defined",
            label_visibility="collapsed"
        )


    # ==================================================
    # ANALYZE BUTTON
    # ==================================================

    st.write("")

    button_col = st.columns([1, 2, 1])[1]

    with button_col:

        analyze = st.button(
            "🔍 Analyze My Error",
            use_container_width=True,
            type="primary"
        )


    # ==================================================
    # ANALYSIS
    # ==================================================

    if analyze:

        if not code.strip() or not error.strip():

            st.warning(
                "⚠️ Please enter both your code and the error message."
            )

        else:

            with st.spinner(
                "🤖 DebugBuddy is thinking..."
            ):

                result = analyze_error(
                    code,
                    error,
                    language=language,
                    mode=mode.lower()
                )


            st.divider()


            # ==================================================
            # DEBUG REPORT
            # ==================================================

            st.markdown(
                '<div class="section-title">🎯 Debug Report</div>',
                unsafe_allow_html=True
            )


            # ==================================================
            # ERROR INFORMATION
            # ==================================================

            info1, info2 = st.columns(2)

            with info1:

                st.markdown(
                    f"### 🔴 {result.get('error_type', 'Unknown')}"
                )

                st.caption("ERROR TYPE")


            with info2:

                line = result.get("line")

                line_text = (
                    "Unknown"
                    if line is None
                    else f"Line {line}"
                )

                st.markdown(
                    f"### 📍 {line_text}"
                )

                st.caption("PROBLEM LOCATION")


            # ==================================================
            # EXPLANATION
            # ==================================================

            st.markdown(
                '<div class="section-title">💡 What Went Wrong?</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-card">
                    {result.get("explanation", "")}
                </div>
                """,
                unsafe_allow_html=True
            )


            # ==================================================
            # HINTS
            # ==================================================

            st.markdown(
                '<div class="section-title">🧩 Debug It Yourself</div>',
                unsafe_allow_html=True
            )

            st.caption(
                "Try solving the problem yourself using the hints below."
            )

            hints = result.get("hints", [])

            if hints:

                for i, hint in enumerate(hints, 1):

                    with st.expander(
                        f"💡 Hint {i}"
                    ):

                        st.write(hint)

            else:

                st.info(
                    "No hints available."
                )


            # ==================================================
            # FIX MODE
            # ==================================================

            if mode == "Fix":

                st.markdown(
                    '<div class="section-title">🔧 Corrected Code</div>',
                    unsafe_allow_html=True
                )

                if result.get("fix"):

                    st.code(
                        result["fix"],
                        language=language.lower()
                    )

                else:

                    st.info(
                        "No corrected code was returned."
                    )


            # ==================================================
            # CONCEPT
            # ==================================================

            st.markdown(
                '<div class="section-title">🧠 What You Learned</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-card">
                    {result.get("concept", "")}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "🎉 Great! Every error is an opportunity to learn."
            )


# ==================================================
# EXPLAIN CODE MODE
# ==================================================

else:

    st.markdown(
        '<div class="section-title">📚 Understand Your Code</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Don't know what a program does? Paste it below and DebugBuddy will explain it in simple language."
    )


    # ==================================================
    # FEATURE CARDS
    # ==================================================

    card1, card2, card3 = st.columns(3)

    with card1:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Purpose</div>
            <div class="feature-description">
                Understand what the program is designed to do.
            </div>
        </div>
        """, unsafe_allow_html=True)


    with card2:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔎</div>
            <div class="feature-title">Breakdown</div>
            <div class="feature-description">
                Understand important lines step-by-step.
            </div>
        </div>
        """, unsafe_allow_html=True)


    with card3:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Concept</div>
            <div class="feature-description">
                Learn the programming idea behind the code.
            </div>
        </div>
        """, unsafe_allow_html=True)


    # ==================================================
    # EXPLAIN CODE EDITOR
    # ==================================================

    st.markdown(
        '<div class="section-title">💻 Your Code</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="code-editor-title">● main.py</div>',
        unsafe_allow_html=True
    )

    ace_mode = {
        "Python": "python",
        "C": "c_cpp",
        "C++": "c_cpp",
        "Java": "java"
    }[language]

    code = st_ace(
        value="""numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)""",
        language=ace_mode,
        theme="dracula",
        key="explain_code_editor",
        height=380,
        font_size=15,
        tab_size=4,
        show_gutter=True,
        show_print_margin=False,
        wrap=False,
        auto_update=True
    )


    # ==================================================
    # EXPLAIN BUTTON
    # ==================================================

    st.write("")

    button_col = st.columns([1, 2, 1])[1]

    with button_col:

        explain = st.button(
            "📚 Explain This Code",
            use_container_width=True,
            type="primary"
        )


    # ==================================================
    # EXPLANATION
    # ==================================================

    if explain:

        if not code.strip():

            st.warning(
                "⚠️ Please enter some code first."
            )

        else:

            with st.spinner(
                "🤖 DebugBuddy is understanding your code..."
            ):

                result = explain_code(
                    code,
                    language=language
                )


            st.divider()


            # ==================================================
            # PURPOSE
            # ==================================================

            st.markdown(
                '<div class="section-title">🎯 What Is This Code For?</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-card">
                    {result.get("purpose", "")}
                </div>
                """,
                unsafe_allow_html=True
            )


            # ==================================================
            # HOW IT WORKS
            # ==================================================

            st.markdown(
                '<div class="section-title">💡 How Does It Work?</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-card">
                    {result.get("explanation", "")}
                </div>
                """,
                unsafe_allow_html=True
            )


            # ==================================================
            # LINE BY LINE
            # ==================================================

            st.markdown(
                '<div class="section-title">🔎 Line-by-Line Explanation</div>',
                unsafe_allow_html=True
            )

            lines = result.get(
                "line_by_line",
                []
            )

            if lines:

                for i, explanation in enumerate(
                    lines,
                    1
                ):

                    with st.expander(
                        f"💻 Line {i}"
                    ):

                        st.write(
                            explanation
                        )

            else:

                st.info(
                    "No line-by-line explanation available."
                )


            # ==================================================
            # OUTPUT
            # ==================================================

            st.markdown(
                '<div class="section-title">🖥️ Expected Output</div>',
                unsafe_allow_html=True
            )

            output = result.get(
                "output",
                ""
            )

            if output:

                st.code(
                    output
                )

            else:

                st.info(
                    "This code does not have a fixed output."
                )


            # ==================================================
            # CONCEPT
            # ==================================================

            st.markdown(
                '<div class="section-title">🧠 Main Concept</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-card">
                    {result.get("concept", "")}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "🎉 Now you know what your code does!"
            )


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    🐞 DebugBuddy &nbsp; • &nbsp;
    <span style="color:#37d978;">
        UNDERSTAND • DEBUG • LEARN
    </span>
    &nbsp; • &nbsp;
    Built for beginner programmers
</div>
""", unsafe_allow_html=True)