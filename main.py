
import tkinter as tk
import random


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
        self.game_running = False

        self.show_start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_start_screen(self):
        self.game_running = False
        self.clear_screen()

        title = tk.Label(
            self.root,
            text="REFLEX CHALLENGE",
            font=("Arial", 32, "bold"),
            fg="#38BDF8",
            bg="#101522"
        )
        title.pack(pady=(100, 20))

        subtitle = tk.Label(
            self.root,
            text="Test your reaction speed!",
            font=("Arial", 16),
            fg="white",
            bg="#101522"
        )
        subtitle.pack(pady=10)

        best = tk.Label(
            self.root,
            text=f"BEST SCORE: {self.best_score}",
            font=("Arial", 14, "bold"),
            fg="#FACC15",
            bg="#101522"
        )
        best.pack(pady=20)

        start_button = tk.Button(
            self.root,
            text="START GAME",
            font=("Arial", 16, "bold"),
            bg="#38BDF8",
            fg="#101522",
            activebackground="#0EA5E9",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=self.start_game
        )
        start_button.pack(pady=20)

    def start_game(self):
        self.cancel_timer()
        self.score = 0
        self.time_left = self.duration
        self.game_running = True

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

    def spawn_target(self):
        if not self.game_running:
            return

        if self.target_id is not None:
            self.game_area.delete(self.target_id)

        radius = random.randint(18, 35)
        x = random.randint(radius, 840 - radius)
        y = random.randint(radius, 480 - radius)

        self.target_id = self.game_area.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=random.choice(["#38BDF8", "#A78BFA", "#34D399"]),
            outline=""
        )

        self.game_area.tag_bind(
            self.target_id,
            "<Button-1>",
            self.hit_target
        )

    def hit_target(self, event):
        if not self.game_running:
            return

        self.score += 10
        self.score_label.config(text=f"SCORE: {self.score}")
        self.spawn_target()

    def update_timer(self):
        if not self.game_running:
            return

        self.timer_label.config(text=f"TIME: {self.time_left}")

        if self.time_left <= 0:
            self.end_game()
            return

        self.time_left -= 1
        self.timer_id = self.root.after(1000, self.update_timer)

    def cancel_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def end_game(self):
        self.game_running = False
        self.cancel_timer()

        if self.score > self.best_score:
            self.best_score = self.score

        self.show_game_over()

    def show_game_over(self):
        self.clear_screen()

        title = tk.Label(
            self.root,
            text="GAME OVER",
            font=("Arial", 32, "bold"),
            fg="#F87171",
            bg="#101522"
        )
        title.pack(pady=(100, 30))

        score = tk.Label(
            self.root,
            text=f"YOUR SCORE: {self.score}",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#101522"
        )
        score.pack(pady=15)

        best = tk.Label(
            self.root,
            text=f"BEST SCORE: {self.best_score}",
            font=("Arial", 16),
            fg="#FACC15",
            bg="#101522"
        )
        best.pack(pady=10)

        play_button = tk.Button(
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
        )
        play_button.pack(pady=30)

        menu_button = tk.Button(
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
        )
        menu_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    game = ReflexChallenge(root)
    root.mainloop()
