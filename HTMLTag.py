class HTMLTag:
    def __init__(self, tag: str, **attributes: str) -> None:
        """
        Type html tags like: div, form, input, select, img, a
        Attributes: e.g. name="main", id="send-button", class="underline"...
        """
        self._tag = tag
        self._attributes = attributes

    @property
    def create_element(self) -> str:
        attributes_str = " ".join(
            [f'{key}="{value}"' for key, value in self._attributes.items()]
        )
        return f"<{self._tag} {attributes_str}>\n"

    @property
    def close_tag(self) -> str:
        """
        Method closing tag
        """
        return f"</{self._tag}>\n"

    @property
    def create_and_close_element(self):
        return self.create_element + self.close_tag


if __name__ == "__main__":
    div_tag = HTMLTag("div", id="main-form")
    form_tag = HTMLTag("form", action="/submit", method="post")
    username_input_tag = HTMLTag("input", type="text", name="username")
    gender_select_tag = HTMLTag("select", name="gender", id="gender")
    a_tag = HTMLTag("a", href="https://google.com")
    img_tag = HTMLTag(
        "img",
        src="img/smile.png",
        alt="Example image",
        width=25,
        height=25,
    )
    br_element = HTMLTag("br")
    label_tag = HTMLTag("label")

    string = (
        div_tag.create_element
        + form_tag.create_element
        + label_tag.create_element
        + "Name: "
        + label_tag.close_tag
        + username_input_tag.create_and_close_element
        + br_element.create_element
        + label_tag.create_element
        + "Gender: "
        + label_tag.close_tag
        + gender_select_tag.create_and_close_element
        + br_element.create_element
        + a_tag.create_element
        + "Link"
        + a_tag.close_tag
        + img_tag.create_and_close_element
        + form_tag.close_tag
        + div_tag.close_tag
    )

    with open("index.html", "w") as file:
        file.write(string)
        print(".html file was created!")
