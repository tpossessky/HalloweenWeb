// Sequential line drawing animation
const lines = [];
const totalLines = 16;
let progress = 0; // Initialize progress variable


function drawLines(timestamp) {
    // Increase progress gradually
    progress += 0.004; // Slightly faster for smoother animation
    if (progress > 1) progress = 1;

    // Update each line
    const totalProgress = progress * totalLines;

    lines.forEach((line, index) => {
        const lineProgress = Math.max(0, Math.min(1, totalProgress - index));
        const drawLength = line.length * lineProgress;
        line.element.style.strokeDashoffset = line.length - drawLength;
    });

    // Continue animation until fully drawn
    if (progress < 1) {
        requestAnimationFrame(drawLines);
    }
}


// Initialize animation when DOM is loaded
window.addEventListener('DOMContentLoaded', () => {
    console.log("DOM loaded, initializing animation...");

    // Wait a brief moment to ensure SVG is fully rendered
    setTimeout(() => {
        for (let i = 0; i < totalLines; i++) {
            const line = document.getElementById(`line${i}`);
            if (!line) {
                console.warn(`Line ${i} not found`);
                continue;
            }
            
            try {
                const length = line.getTotalLength();
                line.style.strokeDasharray = length;
                line.style.strokeDashoffset = length;
                lines.push({ element: line, length: length });
            } catch (error) {
                console.error(`Error initializing line ${i}:`, error);
            }
        }
        
        if (lines.length > 0) {
            requestAnimationFrame(drawLines);
        } else {
            console.error("No lines found to animate");
        }
    }, 100); // Small delay to ensure SVG is ready
});

setTimeout(() => {
    const splash = document.getElementById('splash');

    // Start fade out
    splash.classList.add('fade-out');

    // Wait for CSS fade duration to finish
    setTimeout(() => {
        splash.remove();

        fetch('/home')  // only inner HTML
            .then(response => response.text())
            .then(html => {
                const home = document.getElementById('home-container');
                home.innerHTML = html;
                home.classList.add('visible'); // fade in home
            });

    }, 1000); // matches CSS transition duration
}, 5000); // initial splash delay