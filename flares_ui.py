from typing import Union, Any

class Container_Component:
    @staticmethod
    def Container_Fluid(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 container-fluid element.

        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the container-fluid element.
        :param style: A string or dictionary of CSS styles to apply to the container-fluid element.
        :param child_content: The content to be rendered inside the container-fluid element.
        :return: A string of HTML representing the container-fluid element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<div class="container-fluid {" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</div>'
    
    @staticmethod
    def Container(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 container element.

        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the container element.
        :param style: A string or dictionary of CSS styles to apply to the container element.
        :param child_content: The content to be rendered inside the container element.
        :return: A string of HTML representing the container element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<div class="container {" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</div>'

class GridSystem:
    @staticmethod
    def Row(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 row element.

        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the row element.
        :param style: A string or dictionary of CSS styles to apply to the row element.
        :param child_content: The content to be rendered inside the row element.
        :return: A string of HTML representing the row element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<div class="row {" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</div>'
    
    @staticmethod
    def Col(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "", size: str = "12") -> str:
        """
        Create a Bootstrap 5 column element.

        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the column element.
        :param style: A string or dictionary of CSS styles to apply to the column element.
        :param child_content: The content to be rendered inside the column element.
        :param size: The grid size for the column, typically 1 to 12 for Bootstrap grid.
        :return: A string of HTML representing the column element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<div class="col-{size} {" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</div>'
    
class Typography:
    @staticmethod
    def Heading(level: int = 1, bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 heading element (h1 to h6).
        
        :param level: The heading level (1 to 6).
        :param bs_class: A string or tuple of Bootstrap 5 classes to apply to the heading element.
        :param style: A string or dictionary of CSS styles to apply to the heading element.
        :param child_content: The content to be rendered inside the heading element.
        :return: A string of HTML representing the heading element.
        """
        if level not in range(1, 7):
            raise ValueError("Level must be between 1 and 6.")
        
        tag = f"h{level}"
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<{tag} class="{" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</{tag}>'
    
    @staticmethod
    def Paragraph(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 paragraph element.
        
        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the paragraph element.
        :param style: A string or dictionary of CSS styles to apply to the paragraph element.
        :param child_content: The content to be rendered inside the paragraph element.
        :return: A string of HTML representing the paragraph element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<p class="{" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</p>'
    
    @staticmethod
    def Blockquote(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 blockquote element.
        
        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the blockquote element.
        :param style: A string or dictionary of CSS styles to apply to the blockquote element.
        :param child_content: The content to be rendered inside the blockquote element.
        :return: A string of HTML representing the blockquote element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<blockquote class="{" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</blockquote>'
    
    @staticmethod
    def Lead(bs_class: Union[str, tuple] = "", style: Union[str, dict] = "", child_content: Any = "") -> str:
        """
        Create a Bootstrap 5 lead paragraph element.
        
        :param bs_class: A string or tuple of strings of Bootstrap 5 classes to apply to the lead element.
        :param style: A string or dictionary of CSS styles to apply to the lead element.
        :param child_content: The content to be rendered inside the lead element.
        :return: A string of HTML representing the lead element.
        """
        style_str = (
            '; '.join([f"{key}: {value}" for key, value in style.items()]) + ';' if isinstance(style, dict) else style
        )
        return f'<p class="lead {" ".join(bs_class) if isinstance(bs_class, tuple) else bs_class}" style="{style_str}">{child_content}</p>'