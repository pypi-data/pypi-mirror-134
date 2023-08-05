/*
 * pagemarks - Free git-based, self-hosted bookmarks on the web and via command line
 * Copyright (c) 2019-2021 the pagemarks contributors
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
 * License, version 3, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along with this program.
 * If not, see <https://www.gnu.org/licenses/gpl.html>.
 */

'use strict';


const PM_COLOR_THEME = 'pagemarks-color-theme';  /* name of the localStorage item for the selected color theme */
const PM_DEFAULT_THEME_NAME = 'darkly';


function readThemeNameFromLocalStorage() {
    var themeName = localStorage.getItem(PM_COLOR_THEME);
    if (themeName == null) {
        themeName = PM_DEFAULT_THEME_NAME;
    }
    return themeName;
}


function updateNavbarIcon(themeName) {
    const iconEl = document.getElementById('cssThemeIcon');
    iconEl.classList.remove('oi-sun');
    iconEl.classList.remove('oi-moon');
    iconEl.classList.add('oi-' + exports.css_themes[themeName]);
}


function highlightDropdownList(themeName) {
    var themeList = document.getElementById('navbarColorTheme');
    themeList = themeList.nextSibling.nextSibling.childNodes;   // jump over a text node
    for(var i=0; i<themeList.length; i++) {
        // iterate over anchors
        if (typeof(themeList[i].text) === 'string') {
            const cl = themeList[i].childNodes[2].classList;
            if (themeList[i].text.trim() === themeName) {
                cl.remove('invisible');
                cl.add('visible');
            }
            else {
                cl.remove('visible');
                cl.add('invisible');
            }
        }
    }
}


function switchMainStylesheet(themeName) {
    const styleSheetLink = $('head > link[data-css="main"]');
    const regex = /^(.+?_)[a-z]+\.css$/;
    const m = regex.exec(styleSheetLink.attr('href'))
    var newUrl = styleSheetLink.attr('href');
    if (m !== null) {
        newUrl = m[1] + themeName + '.css';
    }
    styleSheetLink.attr('href', newUrl);
}


exports.setCssTheme = function(themeName)
{
    if (themeName !== undefined) {
        event = event || window.event;
        event.preventDefault();
    }
    themeName = themeName || readThemeNameFromLocalStorage();

    updateNavbarIcon(themeName);
    highlightDropdownList(themeName);
    switchMainStylesheet(themeName);

    localStorage.setItem(PM_COLOR_THEME, themeName);
    setTimeout(() => window.dispatchEvent(new Event('resize')), 100);
    setTimeout(() => window.dispatchEvent(new Event('resize')), 300);
    setTimeout(() => window.dispatchEvent(new Event('resize')), 1500);
}
