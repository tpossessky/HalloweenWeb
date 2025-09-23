// Sequential line drawing animation
const lines = [];
const totalLines = 16;
let progress = 0; // Initialize progress variable

function drawLines(timestamp) {
    progress += 0.004; // Gradually increase progress
    if (progress > 1) progress = 1;

    const totalProgress = progress * totalLines;

    lines.forEach((line, index) => {
        const lineProgress = Math.max(0, Math.min(1, totalProgress - index));
        const drawLength = line.length * lineProgress;
        line.element.style.strokeDashoffset = line.length - drawLength;
    });

    if (progress < 1) {
        requestAnimationFrame(drawLines);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    const splash = document.getElementById('splash');
    const homeContainer = document.getElementById('home-container');

    // Function to show home content after fonts are ready
    function showHome(html) {
        document.fonts.ready.then(() => {
            homeContainer.innerHTML = html;
            homeContainer.classList.add('visible'); // fade in home
        });
    }

    // Fetch home HTML content
    function loadHome() {
        fetch('/home')
        .then(response => response.text())
        .then(html => {
            // Wait for fonts to load first
            document.fonts.ready.then(() => {
                const homeContainer = document.getElementById('home-container');
                homeContainer.innerHTML = html;
                homeContainer.classList.add('visible'); // fade in home
            });
        })
        .catch(err => console.error("Failed to load home:", err));
}

    if (splash) {
        // First visit: animate splash
        setTimeout(() => {
            // Initialize lines and hide them
            for (let i = 0; i < totalLines; i++) {
                const line = document.getElementById(`line${i}`);
                if (!line) continue;
                try {
                    const length = line.getTotalLength();
                    line.style.strokeDasharray = length;
                    line.style.strokeDashoffset = length;
                    lines.push({ element: line, length: length });
                } catch (err) {
                    console.error(`Error initializing line ${i}:`, err);
                }
            }

            if (lines.length > 0) requestAnimationFrame(drawLines);

            // Fade out splash after 5s
            setTimeout(() => {
                splash.classList.add('fade-out');
                setTimeout(() => {
                    splash.remove();
                    loadHome();
                }, 1000); // matches CSS transition duration
            }, 5000); // initial splash delay
        }, 100); // ensure SVG is ready
    } else {
        // Repeat visit: skip splash, show home immediately
        loadHome();
    }
});