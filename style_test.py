"""
Style test scene — preview the visual theme before committing to the full video.

Render with:
    manim -pql style_test.py StyleTest        # quick low-quality preview (480p)
    manim -pqh style_test.py StyleTest        # high-quality 1080p
"""

from manim import *

# ---------- THEME ----------
BG = "#FAFAFA"
INK = "#1F2937"       # primary text
MUTED = "#6B7280"     # secondary text
HAIR = "#E5E7EB"      # hairlines / dividers

# Five accent colors, one per topic
C_CRYPTO = "#F59E0B"      # amber
C_USDT = "#10B981"        # green
C_CHAIN = "#3B82F6"       # blue
C_WALLET = "#8B5CF6"      # purple
C_P2P = "#EC4899"         # pink

FONT_SANS = "Helvetica Neue"

config.background_color = BG
config.frame_rate = 30


def title(text, size=56, color=INK, weight=BOLD):
    return Text(text, font=FONT_SANS, weight=weight, color=color).scale(size / 48)


def body(text, size=28, color=INK, weight=NORMAL):
    return Text(text, font=FONT_SANS, weight=weight, color=color).scale(size / 48)


def caption(text, size=20, color=MUTED, weight=NORMAL):
    return Text(text, font=FONT_SANS, weight=weight, color=color).scale(size / 48)


def chip(label, color):
    """Small rounded chip — used for topic labels."""
    dot = Dot(radius=0.12, color=color)
    txt = body(label, size=22, color=INK)
    g = VGroup(dot, txt).arrange(RIGHT, buff=0.18)
    return g


def block(label, color, w=1.4, h=1.0):
    """Rounded rectangle 'block' used for blockchain-style diagrams."""
    rect = RoundedRectangle(
        width=w, height=h, corner_radius=0.12,
        color=color, stroke_width=3, fill_color=color, fill_opacity=0.08,
    )
    txt = Text(label, font=FONT_SANS, weight=BOLD, color=color).scale(0.32)
    return VGroup(rect, txt)


class StyleTest(Scene):
    def construct(self):
        # ============ BEAT 1 — title card (≈ 4s) ============
        t = title("Crypto, Explained.", size=72)
        s = caption("a visual style preview", size=26)
        VGroup(t, s).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(t, shift=UP * 0.2), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(VGroup(t, s)), run_time=0.5)

        # ============ BEAT 2 — color palette / topic chips (≈ 5s) ============
        header = caption("the five ideas", size=22).to_edge(UP, buff=1.0)

        chips = VGroup(
            chip("crypto",     C_CRYPTO),
            chip("USDT",       C_USDT),
            chip("blockchain", C_CHAIN),
            chip("wallets",    C_WALLET),
            chip("P2P",        C_P2P),
        ).arrange(RIGHT, buff=0.7).move_to(ORIGIN)

        self.play(FadeIn(header), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in chips], lag_ratio=0.12), run_time=1.2)
        self.wait(1.6)
        self.play(FadeOut(VGroup(header, chips)), run_time=0.5)

        # ============ BEAT 3 — wallet → wallet transfer (≈ 6s) ============
        wallet_a = block("WALLET A", C_WALLET, w=2.2, h=1.4)
        wallet_b = block("WALLET B", C_WALLET, w=2.2, h=1.4)
        wallet_a.move_to(LEFT * 3.5)
        wallet_b.move_to(RIGHT * 3.5)

        arrow = Arrow(
            wallet_a.get_right() + RIGHT * 0.15,
            wallet_b.get_left() + LEFT * 0.15,
            buff=0,
            stroke_width=3,
            color=MUTED,
            max_tip_length_to_length_ratio=0.06,
        )

        coin = Circle(radius=0.22, color=C_CRYPTO, stroke_width=3, fill_color=C_CRYPTO, fill_opacity=0.15)
        coin_label = Text("$", font=FONT_SANS, weight=BOLD, color=C_CRYPTO).scale(0.42)
        coin_group = VGroup(coin, coin_label).move_to(wallet_a.get_right() + RIGHT * 0.5)

        send_caption = caption("a transaction", size=22).next_to(arrow, UP, buff=0.25)

        self.play(FadeIn(wallet_a, shift=RIGHT * 0.15), FadeIn(wallet_b, shift=LEFT * 0.15), run_time=0.7)
        self.play(Create(arrow), FadeIn(send_caption), run_time=0.5)
        self.play(FadeIn(coin_group, scale=0.8), run_time=0.4)
        self.play(coin_group.animate.move_to(wallet_b.get_left() + LEFT * 0.5), run_time=1.4, rate_func=smooth)
        self.play(FadeOut(coin_group, scale=0.7), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(VGroup(wallet_a, wallet_b, arrow, send_caption)), run_time=0.5)

        # ============ BEAT 4 — mini blockchain (≈ 6s) ============
        b1 = block("BLOCK 1", C_CHAIN)
        b2 = block("BLOCK 2", C_CHAIN)
        b3 = block("BLOCK 3", C_CHAIN)
        chain = VGroup(b1, b2, b3).arrange(RIGHT, buff=0.9).move_to(ORIGIN)

        link12 = Line(b1.get_right(), b2.get_left(), color=MUTED, stroke_width=2)
        link23 = Line(b2.get_right(), b3.get_left(), color=MUTED, stroke_width=2)

        chain_caption = caption("blocks linked into a chain", size=22).next_to(chain, DOWN, buff=0.6)

        self.play(FadeIn(b1, shift=UP * 0.1), run_time=0.4)
        self.play(Create(link12), FadeIn(b2, shift=UP * 0.1), run_time=0.5)
        self.play(Create(link23), FadeIn(b3, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(chain_caption), run_time=0.4)
        self.wait(1.6)
        self.play(FadeOut(VGroup(b1, b2, b3, link12, link23, chain_caption)), run_time=0.5)

        # ============ BEAT 5 — closing card (≈ 4s) ============
        ask = title("looks good?", size=64)
        sub = caption("if yes, I'll build out all 7 minutes in this exact style", size=22)
        VGroup(ask, sub).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        # tiny accent underline
        underline = Line(
            ask.get_corner(DL) + DOWN * 0.15,
            ask.get_corner(DR) + DOWN * 0.15,
            color=C_USDT,
            stroke_width=4,
        )

        self.play(FadeIn(ask, shift=UP * 0.2), run_time=0.7)
        self.play(Create(underline), FadeIn(sub), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(VGroup(ask, sub, underline)), run_time=0.6)
