import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

class MonteCarloPi:
    """Kelas untuk menghitung estimasi π menggunakan metode Monte Carlo."""

    def __init__(self, num_points: int):
        """Inisialisasi dengan jumlah titik simulasi."""
        self.num_points = num_points
        self.inside_circle = 0
        self.points = None

    def generate_points(self) -> None:
        """Menghasilkan titik acak dan mengklasifikasikannya."""
        # Hasilkan semua titik sekaligus untuk efisiensi lebih baik
        self.points = np.random.uniform(-1, 1, (self.num_points, 2))
        # Hitung titik di dalam lingkaran menggunakan operasi vektor
        distances = np.sum(self.points ** 2, axis=1)
        self.inside_circle = np.sum(distances <= 1)

    def calculate_pi(self) -> float:
        """Menghitung estimasi nilai π."""
        return 4 * (self.inside_circle / self.num_points)

    def get_point_coordinates(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Mengembalikan koordinat titik dalam dan luar lingkaran."""
        mask = np.sum(self.points ** 2, axis=1) <= 1
        inside_points = self.points[mask]
        outside_points = self.points[~mask]
        return (inside_points[:, 0], inside_points[:, 1],
                outside_points[:, 0], outside_points[:, 1])

    def plot_results(self, estimated_pi: float) -> None:
        """Membuat visualisasi hasil simulasi."""
        fig, ax = plt.subplots(figsize=(8, 8))

        # Ambil koordinat untuk plotting
        x_in, y_in, x_out, y_out = self.get_point_coordinates()

        # Plot titik-titik
        ax.scatter(x_in, y_in, c='green', s=1, label='Di Dalam Lingkaran', alpha=0.5)
        ax.scatter(x_out, y_out, c='orange', s=1, label='Di Luar Lingkaran', alpha=0.5)

        # Tambahkan lingkaran
        circle = plt.Circle((0, 0), 1, color='purple', fill=False, lw=2)
        ax.add_patch(circle)

        # Konfigurasi plot
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlabel('Sumbu X')
        ax.set_ylabel('Sumbu Y')
        ax.legend(loc='upper right')
        ax.set_title(f'Estimasi π Monte Carlo ≈ {estimated_pi:.6f}', pad=15)

        # Tambahkan grid
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.show()

def estimate_pi(num_points: int = 10000) -> float:
    """Fungsi utama untuk menjalankan simulasi Monte Carlo."""
    simulator = MonteCarloPi(num_points)
    simulator.generate_points()
    pi_estimate = simulator.calculate_pi()
    simulator.plot_results(pi_estimate)
    return pi_estimate

if __name__ == '__main__':
    # Jalankan simulasi
    estimated_pi = estimate_pi(10000)
    print(f'Nilai estimasi π: {estimated_pi:.6f}')
    print(f'Nilai aktual π: {np.pi:.6f}')
    print(f'Error absolut: {abs(np.pi - estimated_pi):.6f}')
