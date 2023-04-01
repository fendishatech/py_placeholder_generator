import os
from PIL import Image, ImageDraw, ImageFont
from  typing import Tuple, Optional

class PlaceholderGenerator:
    def __init__(
            self, 
            width: int, 
            height: int, 
            fill:Optional[str] = None, 
            text_color:Optional[str] = None, 
            text_size:Optional[int] = None            
        ) -> None:
        
        self.width =  width
        self.height =  height
        self.fill =  fill or '#808080' # Defaults to gray
        self.text_color =  text_color or '#E2E2E2' # Defaults smokey white
        self.text_size =  text_size or 30 # Defaults to 30px

    def generate(self, folder: Optional[str] = None) -> None:
        filename = self._generate_filename(folder)
        image = self._create_image()
        self._add_text(image)
        image.save(filename, 'PNG')

    def _generate_filename(self, folder: Optional[str]) -> str:
        if folder:
            os.makedirs(folder, exist_ok=True)
            filename = os.path.join(folder, f"{self.width}x{self.height}.png")
        else:
            filename = f"{self.width}x{self.height}.png"
        return filename

    def _create_image(self) -> Image:
        image = Image.new('RGB', (self.width, self.height), self._hex_to_rgb(self.fill))
        return image

    def _add_text(self, image: Image) -> None:
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', self.text_size)
        text = f"{self.width}x{self.height}"
        text_width, text_height = draw.textsize(text, font)
        x = (self.width - text_width) // 2
        y = (self.height - text_height) // 2
        draw.text((x, y), text, font=font, fill=self._hex_to_rgb(self.text_color))

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))