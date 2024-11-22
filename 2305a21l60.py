#creating a oc transformer model 2305a21l60 
import streamlit as st
import math as m 

st.markdown('<h1>2305A21L60-PS7 O.C.T.E.C</h1>',unsafe_allow_html=True)
st.markdown('## INPUT PARAMETERS:')
st.markdown('---')

with st.form('form2'):
    col1=st.columns(1)
    V0=st.number_input('V0(V)')
    I0=st.number_input('I0(A)')
    W0=st.number_input('W0(W)')
    if V0 and I0 == 0:
        st.write('invalid inputs')
    submitted=st.form_submit_button('submit')
    

if submitted:
    st.markdown('## OUTPUT PARAMETERS:')
    st.markdown('---')
    cos0 = W0/(V0*I0)
    sin0 = m.sqrt(1-cos0**2)
    Iw = I0 * cos0
    Iu = I0 * sin0
    if V0 and I0 != 0:
        R0 = V0 / Iw
        X0 = V0 / Iu
        st.write('Open circuit Resistance:',R0,'ohm')
        st.write('Open circuit Reactance:',X0,'ohm')
            
        
                
    
    
    