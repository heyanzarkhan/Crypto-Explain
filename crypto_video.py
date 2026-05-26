"""
Crypto, Explained — full 7-section animated video.

Sections (each is its own Scene — render individually, then concatenate):
    1. Intro
    2. WhatIsCrypto
    3. WhatIsUSDT
    4. WhatIsBlockchain
    5. WalletsAndTransactions
    6. WhatIsP2P
    7. Outro

Render all:
    bash render_all.sh

Render one (low quality preview):
    manim -qm crypto_video.py Intro
"""

import numpy as np
from manim import *
from theme import (
    BG, INK, MUTED, HAIR, SOFT_BG,
    C_CRYPTO, C_USDT, C_CHAIN, C_WALLET, C_P2P, C_GOOD, C_BAD,
    FONT_SANS,
    title, body, caption, kicker, chip, block, card,
    thin_arrow, hairline, page_header,
    bank_icon, person_icon, phone_icon, coin_icon, wallet_icon, globe_icon,
    warning_icon, eye_icon, lock_icon, silhouette_icon,
)

config.background_color = BG
config.frame_rate = 30


# =============================================================================
# 1.  INTRO  (≈ 14 s)
# =============================================================================
class Intro(Scene):
    def construct(self):
        # Three opening questions
        q1 = body("What is cryptocurrency?", size=34, color=INK)
        q2 = body("What is a blockchain?",   size=34, color=INK)
        q3 = body("How does money move with no bank?", size=34, color=INK)
        qs = VGroup(q1, q2, q3).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(q1, shift=UP * 0.15), run_time=0.6)
        self.wait(0.6)
        self.play(FadeIn(q2, shift=UP * 0.15), run_time=0.6)
        self.wait(0.6)
        self.play(FadeIn(q3, shift=UP * 0.15), run_time=0.6)
        self.wait(1.4)
        self.play(FadeOut(qs), run_time=0.6)

        # Title card
        t = title("Crypto, Explained.", size=80)
        s = caption("Everything you need to know — in about seven minutes.", size=24)
        VGroup(t, s).arrange(DOWN, buff=0.5).move_to(ORIGIN + UP * 0.2)

        under = Line(
            t.get_corner(DL) + DOWN * 0.18,
            t.get_corner(DR) + DOWN * 0.18,
            color=C_USDT, stroke_width=4,
        )

        self.play(FadeIn(t, shift=UP * 0.2), run_time=0.8)
        self.play(Create(under), FadeIn(s), run_time=0.6)
        self.wait(1.0)

        # Topic chips at the bottom
        chips = VGroup(
            chip("Crypto",     C_CRYPTO),
            chip("USDT",       C_USDT),
            chip("Blockchain", C_CHAIN),
            chip("Wallets",    C_WALLET),
            chip("P2P",        C_P2P),
        ).arrange(RIGHT, buff=0.6).scale(0.95).to_edge(DOWN, buff=0.9)

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in chips],
                              lag_ratio=0.1), run_time=1.0)
        self.wait(4.0)
        self.play(FadeOut(VGroup(t, s, under, chips)), run_time=0.7)


# =============================================================================
# 2.  WHAT IS CRYPTOCURRENCY  (≈ 70 s)
# =============================================================================
class WhatIsCrypto(Scene):
    def construct(self):
        header = page_header("1 · Cryptocurrency", C_CRYPTO)
        self.add(header)

        # ---- BEAT 1: traditional money / bank (≈ 12 s) ----
        bank = bank_icon(color=INK, scale=1.4).move_to(ORIGIN + UP * 0.2)
        bank_label = caption("BANK · GOVERNMENT", size=18).next_to(bank, DOWN, buff=0.4)

        cur1 = title("₹", size=44, color=MUTED).move_to(LEFT * 4 + UP * 1.2)
        cur2 = title("$", size=44, color=MUTED).move_to(RIGHT * 4 + UP * 1.2)
        cur3 = title("€", size=44, color=MUTED).move_to(LEFT * 4 + DOWN * 1.0)
        cur4 = title("¥", size=44, color=MUTED).move_to(RIGHT * 4 + DOWN * 1.0)
        currencies = VGroup(cur1, cur2, cur3, cur4)

        rules = caption("Rules made by someone else", size=22).to_edge(DOWN, buff=0.9)

        self.play(FadeIn(bank, shift=UP * 0.15), FadeIn(bank_label), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in currencies], lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(rules), run_time=0.5)
        self.wait(10.5)
        self.play(FadeOut(VGroup(bank, bank_label, currencies, rules)), run_time=0.7)

        # ---- BEAT 2: crypto is different (≈ 12 s) ----
        big = title("Cryptocurrency", size=60, color=C_CRYPTO).move_to(UP * 0.3)
        tag = caption("Digital · Not printed · Not controlled", size=22).next_to(big, DOWN, buff=0.5)

        self.play(Write(big), run_time=1.0)
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(12.0)
        self.play(FadeOut(VGroup(big, tag)), run_time=0.6)

        # ---- BEAT 3: network of computers + coins (≈ 22 s) ----
        # build a small mesh network of nodes
        rng = np.random.default_rng(7)
        node_positions = [
            np.array([-4.5,  1.2, 0]),
            np.array([-3.0,  2.1, 0]),
            np.array([-1.3,  1.6, 0]),
            np.array([ 0.5,  2.2, 0]),
            np.array([ 2.2,  1.4, 0]),
            np.array([ 4.0,  2.0, 0]),
            np.array([-4.0, -0.3, 0]),
            np.array([-2.0, -0.6, 0]),
            np.array([ 0.0,  0.0, 0]),
            np.array([ 2.0, -0.5, 0]),
            np.array([ 4.2, -0.2, 0]),
            np.array([-3.2, -1.8, 0]),
            np.array([-0.8, -1.7, 0]),
            np.array([ 1.6, -2.0, 0]),
            np.array([ 3.8, -1.7, 0]),
        ]
        nodes = VGroup(*[Dot(p, radius=0.09, color=C_CHAIN) for p in node_positions])

        # connect each node to its 2 nearest neighbors
        lines = VGroup()
        for i, p in enumerate(node_positions):
            dists = sorted(range(len(node_positions)),
                           key=lambda j: np.linalg.norm(node_positions[j] - p))
            for j in dists[1:3]:
                if i < j:
                    lines.add(Line(p, node_positions[j], color=HAIR, stroke_width=1.5))

        net_label = caption("A network of computers around the world", size=22).to_edge(DOWN, buff=0.9)

        self.play(Create(lines, lag_ratio=0.02), run_time=1.2)
        self.play(LaggedStart(*[GrowFromCenter(n) for n in nodes], lag_ratio=0.04), run_time=1.0)
        self.play(FadeIn(net_label), run_time=0.4)
        self.wait(2.5)

        # three coins fly up and arrange — use ticker text (Unicode ₿ doesn't render in all fonts)
        btc = coin_icon("BTC", C_CRYPTO,  scale=1.0)
        eth = coin_icon("ETH", "#627EEA", scale=1.0)
        sol = coin_icon("SOL", "#9945FF", scale=1.0)
        coins = VGroup(btc, eth, sol).arrange(RIGHT, buff=1.4)

        btc_lbl = caption("Bitcoin",  size=18).next_to(btc, DOWN, buff=0.18)
        eth_lbl = caption("Ethereum", size=18).next_to(eth, DOWN, buff=0.18)
        sol_lbl = caption("Solana",   size=18).next_to(sol, DOWN, buff=0.18)

        # group coins with labels
        coin_groups = VGroup(
            VGroup(btc, btc_lbl),
            VGroup(eth, eth_lbl),
            VGroup(sol, sol_lbl),
        )

        # slide the network up to make room
        self.play(
            FadeOut(net_label),
            VGroup(nodes, lines).animate.shift(UP * 0.4).scale(0.85, about_point=ORIGIN + UP * 0.5),
            run_time=0.6,
        )

        coin_groups.move_to(DOWN * 2.7)
        self.play(LaggedStart(
            FadeIn(coin_groups[0], shift=UP * 0.4),
            FadeIn(coin_groups[1], shift=UP * 0.4),
            FadeIn(coin_groups[2], shift=UP * 0.4),
            lag_ratio=0.25,
        ), run_time=1.2)

        more = caption("…and thousands more", size=20).next_to(coin_groups, RIGHT, buff=0.6)
        self.play(FadeIn(more), run_time=0.5)
        self.wait(13.0)

        self.play(FadeOut(VGroup(nodes, lines, coin_groups, more)), run_time=0.7)

        # ---- BEAT 4: send anywhere (≈ 18 s) ----
        ph_a = phone_icon(color=INK, scale=1.3).move_to(LEFT * 4.5)
        ph_b = phone_icon(color=INK, scale=1.3).move_to(RIGHT * 4.5)
        glob = globe_icon(color=MUTED, scale=0.9).move_to(ORIGIN)

        ph_a_label = caption("You", size=18).next_to(ph_a, DOWN, buff=0.3)
        ph_b_label = caption("Anyone, anywhere", size=18).next_to(ph_b, DOWN, buff=0.3)

        self.play(FadeIn(ph_a, shift=RIGHT * 0.15), FadeIn(ph_b, shift=LEFT * 0.15), run_time=0.6)
        self.play(FadeIn(ph_a_label), FadeIn(ph_b_label), FadeIn(glob), run_time=0.5)

        # animate a coin going from phone A across the globe to phone B
        coin = coin_icon("$", C_CRYPTO, scale=0.7).move_to(ph_a.get_top() + UP * 0.1)
        arc = ArcBetweenPoints(
            ph_a.get_top() + UP * 0.2,
            ph_b.get_top() + UP * 0.2,
            angle=-PI / 3,
            color=C_CRYPTO, stroke_width=2,
        )
        # only show the path while the coin travels
        self.play(FadeIn(coin), run_time=0.3)
        self.play(MoveAlongPath(coin, arc), Create(arc), run_time=1.6, rate_func=smooth)
        self.play(FadeOut(coin, scale=0.8), run_time=0.3)

        tagline = body("Anywhere · Anyone · No permission", size=26, color=INK).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(tagline), run_time=0.5)
        self.wait(13.0)

        self.play(FadeOut(VGroup(ph_a, ph_b, glob, ph_a_label, ph_b_label, arc, tagline, header)), run_time=0.7)


# =============================================================================
# 3.  WHAT IS USDT  (≈ 55 s)
# =============================================================================
class WhatIsUSDT(Scene):
    def construct(self):
        header = page_header("2 · USDT (stablecoin)", C_USDT)
        self.add(header)

        # ---- BEAT 1: volatility (≈ 16 s) ----
        axes = Axes(
            x_range=[0, 10, 1], y_range=[-2, 2, 1],
            x_length=8, y_length=3,
            tips=False,
            axis_config={"color": HAIR, "stroke_width": 2,
                         "include_ticks": False, "include_numbers": False},
        ).move_to(UP * 0.4)

        # a wild zig-zag path
        zigzag_xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        zigzag_ys = [0, 1.5, -1.0, 1.8, -0.5, 1.2, -1.6, 1.0, -0.8, 1.5, 0.3]
        zig_points = [axes.c2p(x, y) for x, y in zip(zigzag_xs, zigzag_ys)]
        zigzag = VMobject(color=C_BAD, stroke_width=4)
        zigzag.set_points_smoothly(zig_points)

        zig_label = body("BTC price", size=22, color=C_BAD).next_to(axes, UP, buff=0.3).align_to(axes, LEFT)
        zig_caption = caption("Up… down… up… down…", size=22).next_to(axes, DOWN, buff=0.5)

        self.play(Create(axes), run_time=0.6)
        self.play(FadeIn(zig_label), run_time=0.3)
        self.play(Create(zigzag), run_time=2.2, rate_func=linear)
        self.play(FadeIn(zig_caption), run_time=0.4)
        self.wait(10.5)

        # ---- BEAT 2: enter USDT — flat line (≈ 14 s) ----
        flat_y = 0.3
        flat = Line(axes.c2p(0, flat_y), axes.c2p(10, flat_y), color=C_USDT, stroke_width=4)
        flat_label = body("USDT", size=22, color=C_USDT).next_to(axes, DOWN, buff=0.5).align_to(axes, RIGHT)

        self.play(FadeOut(zig_caption), FadeOut(zigzag), FadeOut(zig_label), run_time=0.5)
        self.play(Create(flat), run_time=1.2)
        self.play(FadeIn(flat_label), run_time=0.4)
        self.wait(1.5)

        # the big equation
        eq = title("1 USDT  =  $1", size=56, color=INK).to_edge(DOWN, buff=1.0)
        eq[0][4:8].set_color(C_USDT)
        self.play(FadeIn(eq, shift=UP * 0.15), run_time=0.8)
        self.wait(13.0)

        self.play(FadeOut(VGroup(axes, flat, flat_label, eq)), run_time=0.6)

        # ---- BEAT 3: use cases / cross-border (≈ 24 s) ----
        glob = globe_icon(color=MUTED, scale=1.5).move_to(ORIGIN)
        self.play(FadeIn(glob), run_time=0.6)

        # USDT coins moving across the globe
        usdt_coin = coin_icon("₮", C_USDT, scale=0.6)
        positions = [
            (LEFT * 4.2 + UP * 1.0, RIGHT * 4.2 + DOWN * 1.0),
            (RIGHT * 4.0 + UP * 1.5, LEFT * 4.0 + DOWN * 0.5),
            (LEFT * 3.5 + DOWN * 1.5, RIGHT * 3.5 + UP * 0.8),
        ]

        for start, end in positions:
            c = usdt_coin.copy().move_to(start)
            arc = ArcBetweenPoints(start, end, angle=-PI / 4, color=C_USDT, stroke_width=2)
            self.play(FadeIn(c), run_time=0.2)
            self.play(MoveAlongPath(c, arc), Create(arc), run_time=1.1, rate_func=smooth)
            self.play(FadeOut(c), FadeOut(arc), run_time=0.2)

        use_cases = VGroup(
            chip("Save",                  C_USDT),
            chip("Trade",                 C_USDT),
            chip("Send across borders",   C_USDT),
        ).arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=0.9)

        self.play(LaggedStart(*[FadeIn(u, shift=UP * 0.15) for u in use_cases], lag_ratio=0.2), run_time=1.0)
        self.wait(15.0)

        self.play(FadeOut(VGroup(glob, use_cases, header)), run_time=0.6)


# =============================================================================
# 4.  WHAT IS BLOCKCHAIN  (≈ 90 s)
# =============================================================================
class WhatIsBlockchain(Scene):
    def construct(self):
        header = page_header("3 · Blockchain", C_CHAIN)
        self.add(header)

        # ---- BEAT 1: the question (≈ 10 s) ----
        q = title("Who keeps track\nof who owns what?", size=44, color=INK).move_to(UP * 0.2)
        self.play(FadeIn(q, shift=UP * 0.2), run_time=0.8)
        self.wait(7.0)

        answer = title("The blockchain.", size=52, color=C_CHAIN)
        self.play(FadeOut(q, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=0.7)
        self.wait(3.5)
        self.play(FadeOut(answer), run_time=0.5)

        # ---- BEAT 2: the notebook (≈ 18 s) ----
        nb = RoundedRectangle(width=4.5, height=3.0, corner_radius=0.12,
                              color=INK, stroke_width=3,
                              fill_color=SOFT_BG, fill_opacity=0.6).move_to(ORIGIN + UP * 0.3)
        nb_spine = Line(nb.get_corner(UL) + RIGHT * 0.25,
                        nb.get_corner(DL) + RIGHT * 0.25,
                        color=MUTED, stroke_width=1.5)
        nb_label = caption("The notebook", size=20).next_to(nb, UP, buff=0.25)

        self.play(FadeIn(nb_label), DrawBorderThenFill(nb), Create(nb_spine), run_time=0.9)

        # transaction lines being written
        tx_lines = []
        tx_texts = [
            "Alice  →  Bob       0.5 BTC",
            "Carol  →  Dave      120 USDT",
            "Eve    →  Frank     0.02 ETH",
            "Greg   →  Hana      40 USDT",
        ]
        y0 = nb.get_top()[1] - 0.6
        for i, tx in enumerate(tx_texts):
            t = Text(tx, font=FONT_SANS, color=INK, weight=NORMAL).scale(0.32)
            t.move_to(nb.get_left() + RIGHT * 0.55 + UP * (y0 - i * 0.45 - nb.get_center()[1]))
            t.align_to(nb.get_left() + RIGHT * 0.55, LEFT)
            tx_lines.append(t)

        for t in tx_lines:
            self.play(Write(t), run_time=0.55)
            self.wait(0.15)
        self.wait(8.0)

        # ---- BEAT 3: many copies, decentralized (≈ 15 s) ----
        sub_caption = caption("Copies exist on thousands of computers", size=22).to_edge(DOWN, buff=0.45)

        # shrink the main notebook and place it at the top, then surround with clones
        main_group = VGroup(nb, nb_spine, *tx_lines)
        self.play(
            main_group.animate.scale(0.42).move_to(UP * 1.4),
            FadeOut(nb_label),
            run_time=0.8,
        )

        clone_positions = [
            LEFT * 5.0 + UP * 1.4,
            RIGHT * 5.0 + UP * 1.4,
            LEFT * 4.6 + DOWN * 1.2,
            ORIGIN + DOWN * 1.2,
            RIGHT * 4.6 + DOWN * 1.2,
        ]
        clones = VGroup()
        for pos in clone_positions:
            c = main_group.copy().move_to(pos)
            clones.add(c)

        self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in clones], lag_ratio=0.1), run_time=1.2)
        self.play(FadeIn(sub_caption), run_time=0.4)
        self.wait(12.0)

        # ---- BEAT 4: pages = blocks, link into chain (≈ 18 s) ----
        self.play(FadeOut(VGroup(clones, sub_caption, main_group)), run_time=0.7)

        block_a = block("BLOCK 1", C_CHAIN, w=1.8, h=1.3)
        block_b = block("BLOCK 2", C_CHAIN, w=1.8, h=1.3)
        block_c = block("BLOCK 3", C_CHAIN, w=1.8, h=1.3)
        block_d = block("BLOCK 4", C_CHAIN, w=1.8, h=1.3)
        chain_g = VGroup(block_a, block_b, block_c, block_d).arrange(RIGHT, buff=0.8).move_to(ORIGIN + UP * 0.2)

        links = VGroup(
            Line(block_a.get_right(), block_b.get_left(), color=MUTED, stroke_width=2),
            Line(block_b.get_right(), block_c.get_left(), color=MUTED, stroke_width=2),
            Line(block_c.get_right(), block_d.get_left(), color=MUTED, stroke_width=2),
        )

        chain_caption = caption("Each page is a block · Linked together", size=22).next_to(chain_g, DOWN, buff=0.7)

        self.play(FadeIn(block_a, shift=UP * 0.1), run_time=0.4)
        for i, (b, l) in enumerate(zip([block_b, block_c, block_d], links)):
            self.play(Create(l), FadeIn(b, shift=UP * 0.1), run_time=0.45)
        self.play(FadeIn(chain_caption), run_time=0.5)
        self.wait(18.0)

        # ---- BEAT 5: tampering fails (≈ 22 s) ----
        self.play(FadeOut(chain_caption), run_time=0.4)

        # try to alter block 2
        hand_label = caption("Trying to change a record…", size=20).next_to(chain_g, DOWN, buff=0.7)
        self.play(FadeIn(hand_label), run_time=0.5)

        # block 2 flashes red
        original_color = C_CHAIN
        bad_rect = block_b[0].copy().set_color(C_BAD).set_fill(C_BAD, opacity=0.15)
        bad_lbl = Text("BLOCK 2", font=FONT_SANS, weight=BOLD, color=C_BAD).scale(0.36).move_to(block_b[1].get_center())
        self.play(Transform(block_b[0], bad_rect), Transform(block_b[1], bad_lbl), run_time=0.6)

        # show many copies rejecting it
        self.play(FadeOut(hand_label), run_time=0.3)
        reject_caption = caption("Every other copy rejects the change", size=22).to_edge(DOWN, buff=1.0)

        # create 6 mini-chains around with green checkmarks
        mini_positions = [
            LEFT * 5.0 + DOWN * 1.5,
            LEFT * 2.8 + DOWN * 2.3,
            RIGHT * 0.0 + DOWN * 2.4,
            RIGHT * 2.8 + DOWN * 2.3,
            RIGHT * 5.0 + DOWN * 1.5,
        ]
        checks = VGroup()
        for pos in mini_positions:
            mini = VGroup(*[
                RoundedRectangle(width=0.32, height=0.32, corner_radius=0.04,
                                 color=C_CHAIN, stroke_width=2,
                                 fill_color=C_CHAIN, fill_opacity=0.1) for _ in range(3)
            ]).arrange(RIGHT, buff=0.08)
            check = Text("✓", font=FONT_SANS, weight=BOLD, color=C_GOOD).scale(0.5)
            check.next_to(mini, UP, buff=0.08)
            checks.add(VGroup(mini, check).move_to(pos))

        self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in checks], lag_ratio=0.1), run_time=1.0)
        self.play(FadeIn(reject_caption), run_time=0.4)
        self.wait(2.0)

        # revert block 2 back to blue
        good_rect = block_b[0].copy().set_color(original_color).set_fill(original_color, opacity=0.08)
        good_lbl = Text("BLOCK 2", font=FONT_SANS, weight=BOLD, color=original_color).scale(0.34)
        good_lbl.move_to(block_b[1].get_center())
        self.play(Transform(block_b[0], good_rect), Transform(block_b[1], good_lbl), run_time=0.6)
        self.wait(13.0)

        # ---- BEAT 6: trustworthy stamp (≈ 7 s) ----
        self.play(FadeOut(VGroup(chain_g, links, checks, reject_caption)), run_time=0.6)
        trust = title("Trustworthy.", size=64, color=C_CHAIN)
        under = Line(trust.get_corner(DL) + DOWN * 0.2, trust.get_corner(DR) + DOWN * 0.2,
                     color=C_USDT, stroke_width=4)
        self.play(FadeIn(trust, shift=UP * 0.15), run_time=0.7)
        self.play(Create(under), run_time=0.4)
        self.wait(7.5)
        self.play(FadeOut(VGroup(trust, under, header)), run_time=0.6)


# =============================================================================
# 5.  WALLETS, TRANSACTIONS, HISTORY  (≈ 90 s)
# =============================================================================
class WalletsAndTransactions(Scene):
    def construct(self):
        header = page_header("4 · Wallet & Transactions", C_WALLET)
        self.add(header)

        # ---- BEAT 1: the wallet (≈ 14 s) ----
        w = wallet_icon(color=C_WALLET, scale=2.2).move_to(ORIGIN + UP * 0.4)
        w_label = caption("A crypto wallet", size=22).next_to(w, DOWN, buff=0.5)
        w_sub = caption("Software · or a small device · that holds your keys", size=20).next_to(w_label, DOWN, buff=0.2)

        self.play(DrawBorderThenFill(w), run_time=0.9)
        self.play(FadeIn(w_label), FadeIn(w_sub), run_time=0.5)
        self.wait(14.0)
        self.play(FadeOut(VGroup(w, w_label, w_sub)), run_time=0.6)

        # ---- BEAT 2: two keys (≈ 18 s) ----
        # PUBLIC key card
        pub_card = card(width=5.0, height=3.2).move_to(LEFT * 3.4)
        pub_eye = eye_icon(color=C_CHAIN, scale=0.6).move_to(pub_card.get_top() + DOWN * 0.55)
        pub_k = kicker("PUBLIC ADDRESS", size=16, color=C_CHAIN).next_to(pub_eye, DOWN, buff=0.2)
        pub_eg = Text("0xA1b2…9F3c", font="Menlo", color=INK, weight=BOLD).scale(0.42)
        pub_eg.move_to(pub_card.get_center() + DOWN * 0.05)
        pub_note = caption("Like an email — share it freely", size=18).move_to(pub_card.get_bottom() + UP * 0.4)

        # PRIVATE key card
        prv_card = card(width=5.0, height=3.2).move_to(RIGHT * 3.4)
        prv_lock = lock_icon(color=C_BAD, scale=0.6).move_to(prv_card.get_top() + DOWN * 0.55)
        prv_k = kicker("PRIVATE KEY", size=16, color=C_BAD).next_to(prv_lock, DOWN, buff=0.2)
        # show as masked
        prv_eg = Text("• • • • • • • • • • • •", font=FONT_SANS, color=INK, weight=BOLD).scale(0.5)
        prv_eg.move_to(prv_card.get_center() + DOWN * 0.05)
        prv_note = caption("Like a password — never share it", size=18).move_to(prv_card.get_bottom() + UP * 0.4)

        self.play(FadeIn(pub_card), FadeIn(prv_card), run_time=0.6)
        self.play(DrawBorderThenFill(pub_eye), DrawBorderThenFill(prv_lock), run_time=0.6)
        self.play(FadeIn(pub_k), FadeIn(prv_k), run_time=0.5)
        self.play(Write(pub_eg), Write(prv_eg), run_time=0.9)
        self.play(FadeIn(pub_note), FadeIn(prv_note), run_time=0.5)
        self.wait(18.0)

        self.play(FadeOut(VGroup(pub_card, pub_eye, pub_k, pub_eg, pub_note,
                                 prv_card, prv_lock, prv_k, prv_eg, prv_note)), run_time=0.6)

        # ---- BEAT 3: a transaction (≈ 14 s) ----
        wa = wallet_icon(color=C_WALLET, scale=1.4).move_to(LEFT * 4)
        wb = wallet_icon(color=C_WALLET, scale=1.4).move_to(RIGHT * 4)
        wa_lbl = caption("WALLET A", size=18).next_to(wa, DOWN, buff=0.3)
        wb_lbl = caption("WALLET B", size=18).next_to(wb, DOWN, buff=0.3)

        arrow = thin_arrow(wa.get_right() + RIGHT * 0.2, wb.get_left() + LEFT * 0.2, color=MUTED)
        amt = body("50 USDT", size=26, color=C_USDT).next_to(arrow, UP, buff=0.25)

        coin = coin_icon("$", C_USDT, scale=0.7).move_to(wa.get_right() + RIGHT * 0.4)

        self.play(FadeIn(wa), FadeIn(wb), FadeIn(wa_lbl), FadeIn(wb_lbl), run_time=0.6)
        self.play(Create(arrow), FadeIn(amt), run_time=0.5)
        self.play(FadeIn(coin), run_time=0.3)
        self.play(coin.animate.move_to(wb.get_left() + LEFT * 0.4), run_time=1.4, rate_func=smooth)
        self.play(FadeOut(coin), run_time=0.3)

        tx_hash = Text("TX  0x4f7c…b21a", font="Menlo", color=MUTED, weight=NORMAL).scale(0.38)
        tx_hash.next_to(arrow, DOWN, buff=0.5)
        forever = caption("Recorded forever", size=22, color=INK).next_to(tx_hash, DOWN, buff=0.3)
        self.play(FadeIn(tx_hash), run_time=0.4)
        self.play(FadeIn(forever), run_time=0.4)
        self.wait(11.0)

        self.play(FadeOut(VGroup(wa, wb, wa_lbl, wb_lbl, arrow, amt, tx_hash, forever)), run_time=0.6)

        # ---- BEAT 4: block explorer (≈ 22 s) ----
        explorer_title = kicker("BLOCK EXPLORER", size=16, color=MUTED).move_to(UP * 2.6 + LEFT * 4)
        url_bar = RoundedRectangle(width=7.0, height=0.5, corner_radius=0.08,
                                   color=HAIR, stroke_width=2, fill_color=BG, fill_opacity=1.0)
        url_bar.move_to(UP * 2.6 + RIGHT * 0.6)
        url_text = Text("etherscan.io / 0xA1b2…9F3c", font="Menlo", color=MUTED).scale(0.32)
        url_text.move_to(url_bar.get_left() + RIGHT * 0.4, aligned_edge=LEFT)

        self.play(FadeIn(explorer_title), FadeIn(url_bar), FadeIn(url_text), run_time=0.5)

        # table header
        headers = VGroup(
            caption("DATE",   size=18, color=MUTED, weight=BOLD),
            caption("FROM",   size=18, color=MUTED, weight=BOLD),
            caption("TO",     size=18, color=MUTED, weight=BOLD),
            caption("AMOUNT", size=18, color=MUTED, weight=BOLD),
        ).arrange(RIGHT, buff=1.6).move_to(UP * 1.6)

        hline_top = Line(LEFT * 6.3, RIGHT * 6.3, color=HAIR, stroke_width=1).next_to(headers, DOWN, buff=0.2)

        rows = [
            ("May 22", "0xA1b2…",  "0xC4d5…",  "+ 50 USDT"),
            ("May 21", "0x77ee…",  "0xA1b2…",  "+ 0.05 ETH"),
            ("May 19", "0xA1b2…",  "0x9aa1…",  "− 120 USDT"),
            ("May 17", "0xA1b2…",  "0xbbf2…",  "− 0.01 BTC"),
        ]
        row_objs = VGroup()
        for i, (d, fr, to, am) in enumerate(rows):
            r = VGroup(
                Text(d,  font="Menlo", color=INK, weight=NORMAL).scale(0.34),
                Text(fr, font="Menlo", color=INK, weight=NORMAL).scale(0.34),
                Text(to, font="Menlo", color=INK, weight=NORMAL).scale(0.34),
                Text(am, font="Menlo",
                     color=(C_GOOD if am.startswith("+") else C_BAD), weight=BOLD).scale(0.34),
            ).arrange(RIGHT, buff=1.6)
            r.move_to(hline_top.get_center() + DOWN * (0.45 + i * 0.55))
            row_objs.add(r)

        # align each cell to the corresponding header column
        for r in row_objs:
            for cell, h in zip(r, headers):
                cell.move_to([h.get_x(), cell.get_y(), 0])

        self.play(FadeIn(headers), Create(hline_top), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in row_objs], lag_ratio=0.18), run_time=1.4)

        public_note = caption("All public · Linked only to addresses · Not real names", size=20).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(public_note), run_time=0.5)
        self.wait(22.0)

        # ---- BEAT 5: transparent yet private (≈ 8 s) ----
        self.play(FadeOut(VGroup(explorer_title, url_bar, url_text, headers, hline_top, row_objs, public_note)),
                  run_time=0.6)

        tp = title("Transparent", size=56, color=C_CHAIN)
        amp = title("yet", size=36, color=MUTED)
        pv = title("Private", size=56, color=C_WALLET)
        phrase = VGroup(tp, amp, pv).arrange(RIGHT, buff=0.55).move_to(ORIGIN + UP * 0.2)

        self.play(FadeIn(tp, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(amp), run_time=0.3)
        self.play(FadeIn(pv, shift=UP * 0.1), run_time=0.6)
        self.wait(7.0)

        self.play(FadeOut(VGroup(tp, amp, pv)), run_time=0.6)

        # ---- BEAT 6: NEW — the risk of permanent history (≈ 25 s) ----
        # Show wallet → permanent history → one transaction later flagged as risky
        risk_title = title("But that has a catch.", size=40, color=INK).move_to(UP * 2.4)
        self.play(FadeIn(risk_title, shift=UP * 0.15), run_time=0.6)
        self.wait(2.0)

        # the wallet at left
        w_small = wallet_icon(color=C_WALLET, scale=1.1).move_to(LEFT * 4.8 + UP * 0.2)
        w_addr = Text("0xA1b2…9F3c", font="Menlo", color=MUTED, weight=BOLD).scale(0.32)
        w_addr.next_to(w_small, DOWN, buff=0.25)
        w_note = caption("Same address forever", size=16).next_to(w_addr, DOWN, buff=0.15)

        # history rows on the right
        hist_rows_data = [
            ("Jan 2024", "+ 50 USDT", C_GOOD, False),
            ("Mar 2024", "− 20 USDT", C_BAD,  False),
            ("Jul 2024", "+ 0.05 ETH", C_GOOD, True),   # this one gets flagged later
            ("Nov 2024", "− 100 USDT", C_BAD, False),
        ]
        hist_rows = VGroup()
        for date, amt, color, _ in hist_rows_data:
            d = Text(date, font="Menlo", color=INK, weight=NORMAL).scale(0.32)
            a = Text(amt,  font="Menlo", color=color, weight=BOLD).scale(0.32)
            row = VGroup(d, a).arrange(RIGHT, buff=1.4)
            hist_rows.add(row)
        hist_rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to(RIGHT * 2.0 + UP * 0.2)

        arrow_to_hist = thin_arrow(
            w_small.get_right() + RIGHT * 0.2,
            hist_rows.get_left() + LEFT * 0.4,
            color=MUTED,
        )

        self.play(FadeIn(w_small), FadeIn(w_addr), FadeIn(w_note), run_time=0.6)
        self.play(Create(arrow_to_hist), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in hist_rows], lag_ratio=0.18), run_time=1.2)
        self.wait(4.0)

        # then later — flag the July row
        flagged_row = hist_rows[2]
        warn = warning_icon(color=C_BAD, scale=0.5).next_to(flagged_row, RIGHT, buff=0.3)
        flag_note = caption("Later linked to illegal activity", size=16, color=C_BAD).next_to(flagged_row, RIGHT, buff=1.0)

        # box highlight on that row
        hi = SurroundingRectangle(flagged_row, color=C_BAD, stroke_width=2, buff=0.12, corner_radius=0.06)

        self.play(FadeIn(warn, scale=0.6), Create(hi), run_time=0.6)
        self.play(FadeIn(flag_note, shift=LEFT * 0.15), run_time=0.5)
        self.wait(4.0)

        risk_sub = caption("Your past is public · and permanent", size=20, color=C_BAD).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(risk_sub), run_time=0.5)
        self.wait(7.0)

        self.play(FadeOut(VGroup(risk_title, w_small, w_addr, w_note,
                                 arrow_to_hist, hist_rows, warn, flag_note, hi, risk_sub, header)), run_time=0.7)


# =============================================================================
# 6.  WHAT IS P2P  (≈ 60 s)
# =============================================================================
class WhatIsP2P(Scene):
    def construct(self):
        header = page_header("5 · Peer to Peer", C_P2P)
        self.add(header)

        # ---- BEAT 1: P2P expands (≈ 5 s) ----
        p2p = title("P2P", size=96, color=C_P2P)
        self.play(Write(p2p), run_time=0.8)
        self.wait(0.8)

        peer_full = title("Peer  to  Peer", size=64, color=C_P2P)
        self.play(ReplacementTransform(p2p, peer_full), run_time=0.8)
        self.wait(2.0)
        self.play(peer_full.animate.scale(0.45).to_edge(UP, buff=1.1), run_time=0.6)

        # ---- BEAT 2: the bank in the middle (≈ 14 s) ----
        pa = person_icon(color=INK, scale=1.5).move_to(LEFT * 4.5)
        pb = person_icon(color=INK, scale=1.5).move_to(RIGHT * 4.5)
        bk = bank_icon(color=INK, scale=0.9).move_to(ORIGIN)

        pa_lbl = caption("You", size=18).next_to(pa, DOWN, buff=0.3)
        pb_lbl = caption("Friend", size=18).next_to(pb, DOWN, buff=0.3)
        bk_lbl = caption("Bank", size=18).next_to(bk, DOWN, buff=0.5)

        arr1 = thin_arrow(pa.get_right() + RIGHT * 0.2, bk.get_left() + LEFT * 0.2, color=MUTED)
        arr2 = thin_arrow(bk.get_right() + RIGHT * 0.2, pb.get_left() + LEFT * 0.2, color=MUTED)

        self.play(FadeIn(pa), FadeIn(pb), FadeIn(pa_lbl), FadeIn(pb_lbl), run_time=0.5)
        self.play(FadeIn(bk), FadeIn(bk_lbl), run_time=0.5)
        self.play(Create(arr1), Create(arr2), run_time=0.7)

        normal_caption = caption("The normal way · A middleman in between", size=22).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(normal_caption), run_time=0.4)
        self.wait(11.0)

        # ---- BEAT 3: cross out the bank (≈ 14 s) ----
        cross1 = Line(bk.get_corner(UL), bk.get_corner(DR), color=C_BAD, stroke_width=5)
        cross2 = Line(bk.get_corner(UR), bk.get_corner(DL), color=C_BAD, stroke_width=5)
        self.play(FadeOut(normal_caption), run_time=0.3)
        self.play(Create(cross1), Create(cross2), run_time=0.6)
        self.wait(0.5)

        # fade bank + arrows, draw direct arrow
        self.play(FadeOut(VGroup(bk, bk_lbl, cross1, cross2, arr1, arr2)), run_time=0.6)
        direct = thin_arrow(pa.get_right() + RIGHT * 0.3, pb.get_left() + LEFT * 0.3, color=C_P2P, stroke_width=4)
        direct_lbl = caption("Direct · Computer to computer", size=22).next_to(direct, UP, buff=0.3)
        self.play(Create(direct), FadeIn(direct_lbl), run_time=0.8)

        # a coin travels directly
        coin = coin_icon("$", C_CRYPTO, scale=0.7).move_to(pa.get_right() + RIGHT * 0.4)
        self.play(FadeIn(coin), run_time=0.3)
        self.play(coin.animate.move_to(pb.get_left() + LEFT * 0.4), run_time=1.4, rate_func=smooth)
        self.play(FadeOut(coin), run_time=0.3)
        self.wait(11.0)

        # ---- BEAT 4: full mesh network (≈ 18 s) ----
        self.play(FadeOut(VGroup(pa, pb, pa_lbl, pb_lbl, direct, direct_lbl)), run_time=0.5)

        # 8 peers in a circle, all connected to each other
        n_peers = 8
        radius = 2.1
        peer_positions = [
            np.array([radius * np.cos(2 * PI * i / n_peers + PI / 2),
                      radius * np.sin(2 * PI * i / n_peers + PI / 2), 0])
            for i in range(n_peers)
        ]

        peer_dots = VGroup(*[Dot(p, radius=0.13, color=C_P2P) for p in peer_positions])
        mesh_lines = VGroup()
        for i in range(n_peers):
            for j in range(i + 1, n_peers):
                mesh_lines.add(Line(peer_positions[i], peer_positions[j],
                                    color=HAIR, stroke_width=1.2))

        mesh_caption = caption("Everyone connected directly · No gatekeepers", size=22).to_edge(DOWN, buff=0.9)

        self.play(Create(mesh_lines, lag_ratio=0.02), run_time=1.4)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in peer_dots], lag_ratio=0.05), run_time=0.9)
        self.play(FadeIn(mesh_caption), run_time=0.4)
        self.wait(15.0)

        # ---- BEAT 5: closing words (≈ 9 s) ----
        self.play(FadeOut(VGroup(mesh_lines, peer_dots, mesh_caption)), run_time=0.5)
        words = VGroup(
            title("Fast",          size=46, color=INK),
            title("Global",        size=46, color=INK),
            title("Open",          size=46, color=INK),
            title("No gatekeepers", size=46, color=C_P2P),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(LaggedStart(*[FadeIn(w, shift=UP * 0.15) for w in words], lag_ratio=0.18), run_time=1.4)
        self.wait(6.5)

        self.play(FadeOut(words), run_time=0.5)

        # ---- BEAT 6: NEW — risk of unknown peers (≈ 22 s) ----
        risk_title = title("But — a peer can be anyone.", size=42, color=INK).move_to(UP * 2.4)
        self.play(FadeIn(risk_title, shift=UP * 0.15), run_time=0.7)
        self.wait(2.0)

        # left = you, right = unknown silhouette
        you = person_icon(color=INK, scale=1.5).move_to(LEFT * 4.0 + DOWN * 0.2)
        you_lbl = caption("You", size=18).next_to(you, DOWN, buff=0.3)

        stranger = silhouette_icon(color=MUTED, scale=1.7).move_to(RIGHT * 4.0 + DOWN * 0.2)
        stranger_lbl = caption("Unknown peer", size=18).next_to(stranger, DOWN, buff=0.3)

        link = thin_arrow(you.get_right() + RIGHT * 0.3, stranger.get_left() + LEFT * 0.3,
                          color=C_P2P, stroke_width=3)

        warn = warning_icon(color=C_BAD, scale=1.0).move_to(link.get_center() + UP * 0.7)

        self.play(FadeIn(you), FadeIn(you_lbl), run_time=0.5)
        self.play(FadeIn(stranger), FadeIn(stranger_lbl), run_time=0.5)
        self.play(Create(link), run_time=0.5)
        self.play(FadeIn(warn, scale=0.6), run_time=0.5)

        risk_lines = VGroup(
            caption("Platforms may not verify who they really are", size=20, color=INK),
            caption("If they do something illegal · your wallet is linked", size=20, color=C_BAD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(risk_lines[0]), run_time=0.5)
        self.wait(5.5)
        self.play(FadeIn(risk_lines[1]), run_time=0.5)
        self.wait(9.0)

        self.play(FadeOut(VGroup(risk_title, you, you_lbl, stranger, stranger_lbl,
                                 link, warn, risk_lines, peer_full, header)), run_time=0.7)


# =============================================================================
# 7.  OUTRO  (≈ 25 s)
# =============================================================================
class Outro(Scene):
    def construct(self):
        kt = kicker("RECAP", size=18, color=MUTED).to_edge(UP, buff=1.0)
        self.play(FadeIn(kt), run_time=0.4)

        items = [
            ("Crypto",       "Digital money — no bank, no government",                C_CRYPTO),
            ("Blockchain",   "The public notebook that tracks everything",            C_CHAIN),
            ("Wallet",       "Holds your keys — public address & private key",        C_WALLET),
            ("Transactions", "Recorded forever · public · traceable to your address", C_WALLET),
            ("USDT",         "A stablecoin — always worth one US dollar",             C_USDT),
            ("P2P",          "Peer to peer — no middleman, but verify who you deal with", C_P2P),
        ]

        rows = VGroup()
        for label, desc, color in items:
            dot = Dot(radius=0.1, color=color)
            lbl = body(label, size=24, color=INK, weight=BOLD)
            sep = caption("—", size=20, color=MUTED)
            ds  = caption(desc, size=22, color=MUTED)
            row = VGroup(dot, lbl, sep, ds).arrange(RIGHT, buff=0.25)
            rows.add(row)
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to(ORIGIN + DOWN * 0.1)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in rows], lag_ratio=0.15), run_time=2.0)
        self.wait(11.0)

        self.play(FadeOut(VGroup(kt, rows)), run_time=0.6)

        # closing title
        t = title("You now understand crypto.", size=52)
        sub = caption("The rest of the space just builds on these ideas.", size=22)
        VGroup(t, sub).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        under = Line(t.get_corner(DL) + DOWN * 0.18, t.get_corner(DR) + DOWN * 0.18,
                     color=C_USDT, stroke_width=4)

        self.play(FadeIn(t, shift=UP * 0.15), run_time=0.8)
        self.play(Create(under), FadeIn(sub), run_time=0.6)
        self.wait(7.0)

        sign = caption("Crypto, Explained.", size=18, color=MUTED).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sign), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(VGroup(t, under, sub, sign)), run_time=0.7)
