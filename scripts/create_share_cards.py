"""Regenerate the two static sharing cards; Pillow is not a site-build dependency."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site/assets/images/social"
SCALE = 2
INK = "#0F172A"
MUTED = "#475569"
BLUE = "#2563EB"
GREEN = "#059669"
PURPLE = "#7C3AED"


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    # The checked-in PNGs are used on all hosts. Regeneration uses Windows fonts.
    path = Path("C:/Windows/Fonts") / ("malgunbd.ttf" if bold else "malgun.ttf")
    return ImageFont.truetype(str(path), size * SCALE)


def create_card(language: str) -> Image.Image:
    canvas = Image.new("RGB", (1200 * SCALE, 630 * SCALE), "#F8FAFC")
    draw = ImageDraw.Draw(canvas)

    def rectangle(box: tuple[int, int, int, int], fill: str, *, outline: str | None = None, radius: int = 0) -> None:
        scaled = tuple(value * SCALE for value in box)
        if radius:
            draw.rounded_rectangle(scaled, radius=radius * SCALE, fill=fill, outline=outline, width=2 * SCALE)
        else:
            draw.rectangle(scaled, fill=fill, outline=outline, width=2 * SCALE)

    def text(x: int, y: int, value: str, size: int, color: str = INK, *, bold: bool = False) -> None:
        draw.text((x * SCALE, y * SCALE), value, font=font(size, bold=bold), fill=color)

    def line(points: list[tuple[int, int]], color: str, width: int = 2) -> None:
        draw.line([(x * SCALE, y * SCALE) for x, y in points], fill=color, width=width * SCALE)

    rectangle((0, 0, 1200, 10), "#4F46E5")
    text(72, 47, "AI MATH GUIDE", 23, "#4338CA", bold=True)
    if language == "ko":
        text(68, 104, "모델 해석을 위한", 58, bold=True)
        text(68, 182, "수학과 방법론", 58, bold=True)
        badge = "무료로 읽기 · 한국어 / English"
        badge_width = 415
        stages = (
            ("기호와 수학", "Notation · Linear algebra"),
            ("Transformer 계산", "Attention · Residual stream"),
            ("모델 해석", "Representations · Interventions"),
        )
    else:
        text(68, 106, "Mathematics for", 55, bold=True)
        text(68, 181, "Model Interpretability", 55, bold=True)
        badge = "Free reading · Korean & English"
        badge_width = 435
        stages = (
            ("Notation & mathematics", "Symbols · Linear algebra"),
            ("Transformer computation", "Attention · Residual stream"),
            ("Model interpretability", "Representations · Interventions"),
        )
    rectangle((72, 287, 72 + badge_width, 333), "#E0E7FF", radius=12)
    text(89, 294, badge, 23, "#3730A3", bold=True)

    # Decorative book cards identify the subject areas, without introducing a lesson figure.
    for y, label, color, fill in (
        (95, "f(x)", BLUE, "#DBEAFE"),
        (177, "Q · K · V", GREEN, "#D1FAE5"),
        (259, "Δ activation", PURPLE, "#EDE9FE"),
    ):
        rectangle((904, y, 1128, y + 65), "#FFFFFF", outline="#CBD5E1", radius=12)
        rectangle((919, y + 14, 925, y + 51), fill, radius=2)
        text(946, y + 13, label, 27, color, bold=True)

    for index, ((title, subtitle), color, fill) in enumerate(zip(stages, (BLUE, GREEN, PURPLE), ("#DBEAFE", "#D1FAE5", "#EDE9FE")), start=1):
        x = 72 + (index - 1) * 368
        rectangle((x, 387, x + 320, 530), "#FFFFFF", outline="#CBD5E1", radius=15)
        rectangle((x + 20, 408, x + 61, 445), fill, radius=8)
        text(x + 28, 411, f"0{index}", 20, color, bold=True)
        text(x + 20, 460, title, 24 if language == "ko" else 21, color, bold=True)
        text(x + 20, 495, subtitle, 16, MUTED)
        if index < 3:
            line([(x + 335, 458), (x + 353, 458)], "#64748B", 2)
            line([(x + 347, 452), (x + 353, 458), (x + 347, 464)], "#64748B", 2)

    text(72, 568, "leeklim.github.io/ai-math-guide/" + ("en/" if language == "en" else ""), 21, MUTED)
    return canvas.resize((1200, 630), Image.Resampling.LANCZOS)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for language in ("ko", "en"):
        path = OUTPUT / f"ai-math-guide-{language}.png"
        create_card(language).save(path, optimize=True)
        print(path.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
