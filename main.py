
import tkinter as tk
import random
import math


class ReflexChallenge:
    def __init__(self, root):
        self.root = root
        self.root.title("Reflex Challenge")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#101522")

        self.duration = 30
        self.time_left = self.duration
        self.score = 0
        self.best_score = 0

        self.target_id = None
        self.timer_id = None
        self.animation_ids = set()
        self.game_running = False

        self.show_start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def cancel_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def cancel_animations(self):
        for animation_id in self.animation_ids:
            self.root.after_cancel(animation_id)

        self.animation_ids.clear()

    def show_start_screen(self):
        self.game_running = False
        self.cancel_timer()
        self.cancel_animations()
        self.clear_screen()

        tk.Label(
            self.root,
            text="REFLEX CHALLENGE",
            font=("Arial", 32, "bold"),
            fg="#38BDF8",
            bg="#101522"
        ).pack(pady=(100, 20))

        tk.Label(
            self.root,
            text="Test your reaction speed!",
            font=("Arial", 16),
            fg="white",
            bg="#101522"
        ).pack(pady=10)

        tk.Label(
            self.root,
            text=f"BEST SCORE: {self.best_score}",
            font=("Arial", 14, "bold"),
            fg="#FACC15",
            bg="#101522"
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="START GAME",
            font=("Arial", 16, "bold"),
            bg="#38BDF8",
            fg="#101522",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=self.start_game
        ).pack(pady=20)

    def start_game(self):
        self.cancel_timer()
        self.cancel_animations()

        self.score = 0
        self.time_left = self.duration
        self.game_running = True
        self.target_id = None

        self.clear_screen()

        header = tk.Frame(self.root, bg="#101522")
        header.pack(fill="x", padx=30, pady=20)

        self.score_label = tk.Label(
            header,
            text="SCORE: 0",
            font=("Arial", 16, "bold"),
            fg="#38BDF8",
            bg="#101522"
        )
        self.score_label.pack(side="left")

        self.timer_label = tk.Label(
            header,
            text=f"TIME: {self.time_left}",
            font=("Arial", 16, "bold"),
            fg="#FACC15",
            bg="#101522"
        )
        self.timer_label.pack(side="right")

        self.game_area = tk.Canvas(
            self.root,
            width=840,
            height=480,
            bg="#1E293B",
            highlightthickness=0
        )
        self.game_area.pack(padx=30, pady=10)

        self.spawn_target()
        self.update_timer()

    def get_target_radius(self):
        # Random sizes make targets unpredictable while difficulty increases.
        reduction = self.score // 100

        max_radius = max(25, 45 - reduction)
        min_radius = max(12, 18 - reduction)

        return random.randint(min_radius, max_radius)

    def spawn_target(self):
        if not self.game_running:
            return

        if self.target_id is not None:
            self.game_area.delete(self.target_id)

        radius = self.get_target_radius()

        x = random.randint(radius, 840 - radius)
        y = random.randint(radius, 480 - radius)

        self.target_id = self.game_area.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=random.choice([
                "#38BDF8",
                "#A78BFA",
                "#34D399"
            ]),
            outline=""
        )

        self.game_area.tag_bind(
            self.target_id,
            "<Button-1>",
            self.hit_target
        )

        # Keep the target clickable even when particles overlap it.
        self.game_area.tag_raise(self.target_id)

    def schedule_animation(self, delay, callback):
        # Track callbacks to stop animations safely when the game ends.
        holder = {}

        def execute():
            animation_id = holder["id"]
            self.animation_ids.discard(animation_id)

            if self.game_running:
                callback()

        animation_id = self.root.after(delay, execute)
        holder["id"] = animation_id
        self.animation_ids.add(animation_id)

    def show_fireworks(self, x, y):
        if not self.game_running:
            return

        colors = [
            "#FACC15",
            "#38BDF8",
            "#A78BFA",
            "#34D399",
            "#FB7185"
        ]

        particles = []
        particle_count = 14

        for index in range(particle_count):
            angle = (2 * math.pi * index / particle_count)
            angle += random.uniform(-0.15, 0.15)

            speed = random.uniform(3, 6)
            size = random.randint(2, 4)

            particle_id = self.game_area.create_oval(
                x - size,
                y - size,
                x + size,
                y + size,
                fill=random.choice(colors),
                outline="",
                tags="effect"
            )

            particles.append({
                "id": particle_id,
                "dx": math.cos(angle) * speed,
                "dy": math.sin(angle) * speed
            })

        text_id = self.game_area.create_text(
            x,
            y - 20,
            text="+10",
            fill="#FACC15",
            font=("Arial", 18, "bold"),
            tags="effect"
        )

        total_frames = 10

        def animate(frame):
            if not self.game_running:
                return

            if frame >= total_frames:
                for particle in particles:
                    self.game_area.delete(particle["id"])

                self.game_area.delete(text_id)
                return

            for particle in particles:
                self.game_area.move(
                    particle["id"],
                    particle["dx"],
                    particle["dy"]
                )

                # Slow particles gradually to simulate a small explosion.
                particle["dx"] *= 0.90
                particle["dy"] *= 0.90

                if frame >= 6:
                    self.game_area.itemconfig(
                        particle["id"],
                        state="hidden"
                    )

            self.game_area.move(text_id, 0, -1.5)

            if frame >= 8:
                self.game_area.itemconfig(
                    text_id,
                    state="hidden"
                )

            self.schedule_animation(
                50,
                lambda: animate(frame + 1)
            )

        animate(0)

    def hit_target(self, event):
        if not self.game_running:
            return

        self.score += 10

        self.score_label.config(
            text=f"SCORE: {self.score}"
        )

        self.show_fireworks(event.x, event.y)
        self.spawn_target()

    def update_timer(self):
        if not self.game_running:
            return

        self.timer_label.config(
            text=f"TIME: {self.time_left}"
        )

        if self.time_left <= 0:
            self.end_game()
            return

        self.time_left -= 1

        self.timer_id = self.root.after(
            1000,
            self.update_timer
        )

    def end_game(self):
        self.game_running = False

        self.cancel_timer()
        self.cancel_animations()

        new_record = self.score > self.best_score

        if new_record:
            self.best_score = self.score

        self.show_game_over(new_record)

    def show_game_over(self, new_record):
        self.clear_screen()

        title_color = "#FACC15" if new_record else "#F87171"

        tk.Label(
            self.root,
            text="NEW RECORD!" if new_record else "GAME OVER",
            font=("Arial", 32, "bold"),
            fg=title_color,
            bg="#101522"
        ).pack(pady=(90, 30))

        tk.Label(
            self.root,
            text=f"YOUR SCORE: {self.score}",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#101522"
        ).pack(pady=15)

        tk.Label(
            self.root,
            text=f"BEST SCORE: {self.best_score}",
            font=("Arial", 18, "bold"),
            fg="#FACC15",
            bg="#101522"
        ).pack(pady=10)

        message = (
            "Congratulations! You beat your record!"
            if new_record
            else "Keep practicing to beat your best score!"
        )

        tk.Label(
            self.root,
            text=message,
            font=("Arial", 13),
            fg="#CBD5E1",
            bg="#101522"
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="PLAY AGAIN",
            font=("Arial", 16, "bold"),
            bg="#38BDF8",
            fg="#101522",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=self.start_game
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="MAIN MENU",
            font=("Arial", 12),
            bg="#334155",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            command=self.show_start_screen
        ).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    game = ReflexChallenge(root)
    root.mainloop()
