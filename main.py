from manim import *
import numpy as np

class VectorField(Scene):
    def construct(self):
        matrixA = np.array([[0.2, 0.6], [0.8, 0.4]])

        np.random.seed(42)
        numDots = 30
        dots = VGroup()
        for i in range(numDots):
            x, y = np.random.uniform(-3, 3, size=2)
            dot = Dot(point=[x, y, 0], radius=0.05, color=PURE_BLUE)
            dots.add(dot)
        
        self.add(dots)

        def applyTransform(dotGroup):
            for dot in dotGroup:
                pos = dot.get_center()[:2]
                newPos = matrixA @ pos
                dot.move_to([*newPos, 0])

        self.wait(1)
        self.play(
            UpdateFromAlphaFunc(
                dots,
                lambda mobj, alpha: applyTransform(mobj),
            ),
            run_time=3,
        )
        self.wait(4)