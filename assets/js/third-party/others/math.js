/* Math render plugin */
NexT.plugins.others.math = function () {

    const render_js = NexT.utils.getCDNResource(NexT.CONFIG.page.math.js);
    NexT.utils.getScript(render_js, function () {
        window.MathJax = {
            options: {
                // Don't render math in mindmaps as Markmap has its own math renderer.
                ignoreHtmlClass: 'markmap',
            },
            // asciimath: {
            //     inlineMath: [
            //         ['$', '$'],
            //         ['\\(', '\\)'],
            //     ],
            //     displayMath: [
            //         ['$$', '$$'],
            //         ['\\[', '\\]'],
            //     ],
            //     processEscapes: false,
            //     // packages: {'[+]': ['noerrors']},
            // },
            loader: {
                load: ['input/asciimath'],
            },
        };
    });
}