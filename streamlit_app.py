import streamlit as st

st.set_page_config(page_title="Calculator")

st.title("Quick Calc")
st.caption("Muhammad Saadi | ID: 2540018")

c1, c2 = st.columns(2)

with c1:
    val_a = st.number_input("First Value", value=0.0)

with c2:
    val_b = st.number_input("Second Value", value=0.0)

mode = st.radio(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"],
    horizontal=True
)

if st.button("Get Result", type="primary"):
    ans = None
    
    if mode == "Add":
        ans = val_a + val_b
    elif mode == "Subtract":
        ans = val_a - val_b
    elif mode == "Multiply":
        ans = val_a * val_b
    elif mode == "Divide":
        if val_b == 0:
            st.error("Cannot divide by zero")
        else:
            ans = val_a / val_b

    if ans is not None:
        st.success(f"Output: {ans}")
