"""
Shared theme + helpers for the crypto-explain video.
Light minimal style — off-white background, slate text, 5 accent colors.
"""

from manim import *

# ---------- COLORS ----------
BG = "#FAFAFA"
INK = "#1F2937"       # primary text
MUTED = "#6B7280"     # secondary text / hairlines
HAIR = "#E5E7EB"      # very light dividers
SOFT_BG = "#F3F4F6"   # subtle card fills

# One accent per topic
C_CRYPTO = "#F59E0B"      # amber
C_USDT   = "#10B981"      # green
C_CHAIN  = "#3B82F6"      # blue
C_WALLET = "#8B5CF6"      # purple
C_P2P    = "#EC4899"      # pink

# Semantic colors
C_GOOD = "#10B981"
C_BAD  = "#EF4444"

FONT_SANS = "Helvetica Neue"


# ---------- TEXT HELPERS ----------
def title(text, size=64, color=INK, weight=BOLD):
    return Text(text, font=FONT_SANS, weight=weight, color=color).scale(size / 48)


def body(text, size=28, color=INK, weight=NORMAL):
    return Text(text, font=FONT_SANS, weight=weight, color=color).scale(size / 48)


def caption(text, size=20, color=MUTED, weight=NORMAL):
    return Text(text, font=FONT_SANS, weight=weight, color=color).scale(size / 48)


def kicker(text, size=18, color=MUTED, weight=BOLD):
    """Small uppercase label that sits above a heading."""
    return Text(text.upper(), font=FONT_SANS, weight=weight, color=color).scale(size / 48)


# ---------- SHAPE HELPERS ----------
def chip(label, color, size=22):
    dot = Dot(radius=0.12, color=color)
    txt = body(label, size=size, color=INK)
    return VGroup(dot, txt).arrange(RIGHT, buff=0.18)


def block(label, color, w=1.6, h=1.1, label_scale=0.34, sub=None):
    """Rounded rectangle 'block' with label."""
    rect = RoundedRectangle(
        width=w, height=h, corner_radius=0.12,
        color=color, stroke_width=3, fill_color=color, fill_opacity=0.08,
    )
    t = Text(label, font=FONT_SANS, weight=BOLD, color=color).scale(label_scale)
    items = [rect, t]
    if sub is not None:
        s = Text(sub, font=FONT_SANS, weight=NORMAL, color=MUTED).scale(0.22)
        s.next_to(t, DOWN, buff=0.12)
        items.append(s)
    g = VGroup(*items)
    t.move_to(rect.get_center() if sub is None else rect.get_center() + UP * 0.12)
    if sub is not None:
        s.move_to(rect.get_center() + DOWN * 0.18)
    return g


def card(width=4.5, height=2.6, color=HAIR, fill=SOFT_BG, fill_opacity=0.6, corner_radius=0.18):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        color=color, stroke_width=2, fill_color=fill, fill_opacity=fill_opacity,
    )


def thin_arrow(start, end, color=MUTED, stroke_width=3):
    return Arrow(
        start, end, buff=0,
        stroke_width=stroke_width,
        color=color,
        max_tip_length_to_length_ratio=0.06,
        max_stroke_width_to_length_ratio=8,
    )


def hairline(width=10, color=HAIR):
    return Line(LEFT * width / 2, RIGHT * width / 2, color=color, stroke_width=1.5)


def page_header(label_text, color):
    """A small colored tab + label that sits at the top-left of every section."""
    tab = RoundedRectangle(
        width=0.25, height=0.55, corner_radius=0.06,
        color=color, stroke_width=0, fill_color=color, fill_opacity=1.0,
    )
    txt = kicker(label_text, size=18, color=INK)
    g = VGroup(tab, txt).arrange(RIGHT, buff=0.25)
    g.to_corner(UL, buff=0.55)
    return g


# ---------- ICON HELPERS ----------
def bank_icon(color=INK, scale=1.0):
    """Simple bank: triangle pediment + columns + base."""
    base = Rectangle(width=2.0, height=0.18, color=color, stroke_width=3,
                     fill_color=color, fill_opacity=0.05)
    base.shift(DOWN * 0.85)

    cols = VGroup(*[
        Rectangle(width=0.18, height=1.2, color=color, stroke_width=3,
                  fill_color=color, fill_opacity=0.05).shift(RIGHT * (x - 0.75) + DOWN * 0.18)
        for x in [0, 0.5, 1.0, 1.5]
    ])

    pediment = Polygon(
        LEFT * 1.1 + UP * 0.55,
        RIGHT * 1.1 + UP * 0.55,
        ORIGIN + UP * 1.15,
        color=color, stroke_width=3, fill_color=color, fill_opacity=0.05,
    )
    lintel = Rectangle(width=2.2, height=0.16, color=color, stroke_width=3,
                       fill_color=color, fill_opacity=0.05).shift(UP * 0.5)

    g = VGroup(pediment, lintel, cols, base)
    return g.scale(scale)


def person_icon(color=INK, scale=1.0):
    head = Circle(radius=0.18, color=color, stroke_width=3, fill_color=color, fill_opacity=0.1).shift(UP * 0.45)
    body_arc = ArcBetweenPoints(
        LEFT * 0.32 + DOWN * 0.1, RIGHT * 0.32 + DOWN * 0.1,
        angle=-PI * 0.65, color=color, stroke_width=3,
    )
    return VGroup(head, body_arc).scale(scale)


def phone_icon(color=INK, scale=1.0):
    outer = RoundedRectangle(width=0.9, height=1.6, corner_radius=0.14,
                             color=color, stroke_width=3,
                             fill_color=color, fill_opacity=0.05)
    screen = RoundedRectangle(width=0.74, height=1.25, corner_radius=0.06,
                              color=color, stroke_width=2,
                              fill_color=BG, fill_opacity=1.0)
    home = Line(LEFT * 0.12, RIGHT * 0.12, color=color, stroke_width=2).shift(DOWN * 0.66)
    return VGroup(outer, screen, home).scale(scale)


def coin_icon(symbol="$", color=C_CRYPTO, scale=1.0):
    # bigger coin so 3-letter tickers (BTC, ETH, SOL) fit comfortably
    c = Circle(radius=0.42, color=color, stroke_width=3, fill_color=color, fill_opacity=0.15)
    text_scale = 0.55 if len(symbol) <= 1 else 0.40
    t = Text(symbol, font=FONT_SANS, weight=BOLD, color=color).scale(text_scale)
    return VGroup(c, t).scale(scale)


def warning_icon(color="#EF4444", scale=1.0):
    """Triangle with exclamation — used for risk callouts."""
    tri = Polygon(
        LEFT * 0.5 + DOWN * 0.4,
        RIGHT * 0.5 + DOWN * 0.4,
        UP * 0.55,
        color=color, stroke_width=3, fill_color=color, fill_opacity=0.12,
    )
    bang = Text("!", font=FONT_SANS, weight=BOLD, color=color).scale(0.5)
    bang.move_to(tri.get_center() + DOWN * 0.05)
    return VGroup(tri, bang).scale(scale)


def eye_icon(color=INK, scale=1.0):
    """Eye — used to suggest 'visible / watchable'."""
    outer = Ellipse(width=1.2, height=0.6, color=color, stroke_width=3,
                    fill_color=color, fill_opacity=0.05)
    pupil = Circle(radius=0.16, color=color, stroke_width=3,
                   fill_color=color, fill_opacity=0.6)
    return VGroup(outer, pupil).scale(scale)


def lock_icon(color=INK, scale=1.0):
    """Padlock — used for keys / privacy."""
    body_rect = RoundedRectangle(width=0.85, height=0.7, corner_radius=0.08,
                                 color=color, stroke_width=3,
                                 fill_color=color, fill_opacity=0.08)
    shackle = Arc(radius=0.28, angle=PI, color=color, stroke_width=3)
    shackle.next_to(body_rect, UP, buff=-0.04)
    keyhole = Circle(radius=0.06, color=color, stroke_width=2,
                     fill_color=color, fill_opacity=1.0)
    keyhole.move_to(body_rect.get_center())
    return VGroup(shackle, body_rect, keyhole).scale(scale)


def silhouette_icon(color=MUTED, scale=1.0):
    """A faceless 'unknown person' — for the unknown-peer risk callout."""
    head = Circle(radius=0.22, color=color, stroke_width=0,
                  fill_color=color, fill_opacity=0.4).shift(UP * 0.5)
    body = ArcBetweenPoints(
        LEFT * 0.42 + DOWN * 0.1, RIGHT * 0.42 + DOWN * 0.1,
        angle=-PI * 0.6, color=color, stroke_width=0,
    )
    body.set_fill(color, opacity=0.4)
    q = Text("?", font=FONT_SANS, weight=BOLD, color=BG).scale(0.32).move_to(head.get_center())
    return VGroup(body, head, q).scale(scale)


def wallet_icon(color=C_WALLET, scale=1.0):
    body_rect = RoundedRectangle(width=1.6, height=1.1, corner_radius=0.12,
                                 color=color, stroke_width=3,
                                 fill_color=color, fill_opacity=0.08)
    flap = RoundedRectangle(width=0.45, height=0.35, corner_radius=0.06,
                            color=color, stroke_width=3,
                            fill_color=color, fill_opacity=0.18).shift(RIGHT * 0.45 + DOWN * 0.05)
    return VGroup(body_rect, flap).scale(scale)


def globe_icon(color=INK, scale=1.0):
    circ = Circle(radius=0.9, color=color, stroke_width=3,
                  fill_color=color, fill_opacity=0.04)
    h = Line(LEFT * 0.9, RIGHT * 0.9, color=color, stroke_width=2)
    v = Line(UP * 0.9, DOWN * 0.9, color=color, stroke_width=2)
    e1 = Ellipse(width=1.8, height=0.7, color=color, stroke_width=2)
    e2 = Ellipse(width=0.7, height=1.8, color=color, stroke_width=2)
    return VGroup(circ, h, v, e1, e2).scale(scale)
