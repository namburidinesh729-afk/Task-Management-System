def metric_card(title, value, color="#2563eb"):

    return f"""
<div style="
background:#1f2937;
padding:20px;
border-radius:15px;
border-left:6px solid {color};
text-align:center;
">

<h4 style="color:#9ca3af;margin-bottom:10px;">
{title}
</h4>

<h1 style="color:white;margin:0;">
{value}
</h1>

</div>
"""