import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from flares_ui import Container_Component, GridSystem, Typography

container_component = Container_Component
gridsystem = GridSystem
typography = Typography

app = FastAPI()

@app.get('/')
async def complex_ui():
    html_component = container_component.Container_Fluid(
        bs_class=("p-3", "bg-light"),
        style="min-height: 100vh;",
        child_content=container_component.Container(
            bs_class=("py-5", "my-3"),
            style={
                "font-family": "'Inter', sans-serif",
                "background-color": "#fff",
                "border-radius": "8px",
                "box-shadow": "0 0 15px rgba(0, 0, 0, 0.1)"
            },
            child_content=gridsystem.Row(
                bs_class=("gx-5",),
                child_content=gridsystem.Col(
                    bs_class=("col-md-6", "mb-4"),
                    child_content=typography.Heading(
                        level=2,
                        bs_class=("text-center", "text-primary"),
                        style="font-weight: 600;",
                        child_content="Welcome to the Flares UI!"
                    ) +
                    typography.Paragraph(
                        bs_class=("text-center",),
                        style="font-size: 1.1rem; color: #333;",
                        child_content="This is an example of a more complex layout using Flask, Bootstrap, and custom Flares UI components."
                    )
                ) +
                gridsystem.Col(
                    bs_class=("col-md-6", "mb-4"),
                    child_content=typography.Heading(
                        level=3,
                        bs_class=("text-center", "text-success"),
                        style="font-weight: 500;",
                        child_content="What We Do"
                    ) +
                    typography.Blockquote(
                        bs_class=("blockquote", "text-center", "font-italic"),
                        style="font-size: 1.2rem; color: #555;",
                        child_content="Delivering top-quality solutions, one project at a time."
                    ) +
                    typography.Lead(
                        bs_class=("text-center",),
                        style="font-size: 1.3rem; font-weight: 400; color: #444;",
                        child_content="Our team of experts works tirelessly to meet the needs of our clients."
                    )
                )
            )
        )
    )
    
    return HTMLResponse(content=f"""
        <html>
            <head>
                <title>Flares UI Example</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>{html_component}</body>
        </html>
    """)

if __name__ == '__main__':
    uvicorn.run("app:app", reload=True, reload_includes=["*.py"])