document.addEventListener('DOMContentLoaded', function () {
    var moonSunIcons = document.querySelectorAll('#moon-sun-icon');

    moonSunIcons.forEach(function (moonSunIcon) {
        var themeContainer = moonSunIcon.closest('.theme');
        var themeScreenshot = themeContainer.querySelector('.theme-screenshot');
        var defaultImagePath = themeScreenshot.getAttribute('src');
        var isMoon = moonSunIcon.getAttribute('alt') === 'Moon Icon';

        moonSunIcon.addEventListener('click', function () {
            isMoon = !isMoon;

            var newSrc, altText, iconSize;

            if (defaultImagePath.endsWith('-dark.webp')) {
                newSrc = defaultImagePath.replace('-dark.webp', '.webp');
            } else {
                newSrc = defaultImagePath.replace('.webp', '-dark.webp');
            }

            themeScreenshot.setAttribute('srcset', isMoon ? newSrc : defaultImagePath);

            moonSunIcon.src = isMoon ? './images/moon.svg' : './images/day-sunny.svg';
            altText = isMoon ? 'Moon Icon' : 'Sun Icon';
            iconSize = isMoon ? '35' : '38';

            moonSunIcon.setAttribute('alt', altText);
            moonSunIcon.setAttribute('height', iconSize);
            moonSunIcon.setAttribute('width', iconSize);

            themeContainer.dataset.theme = isMoon ? 'dark' : 'light'; // Use data- attribute to store theme
        });
    });
});
