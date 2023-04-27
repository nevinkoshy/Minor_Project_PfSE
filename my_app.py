import streamlit as st
import plotly.graph_objects as go
import forallpeople as si
from app_module import calc_Pr
from app_module import calc_Pr_list

si.environment("structural")

thickness_value = st.sidebar.number_input("Thickness (mm)", value=200, step=50)
length_value = st.sidebar.number_input("Length (mm)", value=2000, step=50)
height_value = st.sidebar.number_input("Unsupported height (mm)", value=3000, step=50)
k = st.sidebar.number_input("k", value=1.0, step=0.1)
fc_value = st.sidebar.number_input("f'c (MPa)", value=40, step=5)

t=0
phi_c = 0.65

t = thickness_value * si.mm
length = length_value * si.mm
hu = height_value * si.mm
fc = fc_value * si.MPa

Pr_latex, Pr_value = calc_Pr(t, length, hu, k, phi_c, fc)

st.markdown("# Axial capacity of a concrete bearing wall")
st.latex(Pr_latex)

st.markdown("# Investigation")

st.sidebar.header("Investigation:")

t_values = st.sidebar.slider(
    'Wall thickness:',
    150, 900, (200, 300), step=50)
t_start, t_end = t_values
thick_list= list(range(t_start, t_end+50,50))

Pr_list = calc_Pr_list(thick_list, length_value, height_value, k, phi_c, fc_value)
# st.sidebar.write(thick_list)
# st.sidebar.write(Pr_list)

fig = go.Figure()

# Plot lines
# for value in t_values:
fig.add_trace(
    go.Scatter(
    x=t_values, 
    y=Pr_list,
    # line={"color": 1},
    name="Column A"
    )
)

# fig.layout.title.text = "Bearing wall"
fig.layout.xaxis.title = "Thickness of wall, mm"
fig.layout.yaxis.title = "Pr, MN"

st.plotly_chart(fig)
