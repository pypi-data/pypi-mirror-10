/**
 * .. class:: Widgets.TimelineWidget
 *
 * widget based on SIMILE's timeline widget
 * http://code.google.com/p/simile-widgets/
 *
 * Beware not to mess with SIMILE's Timeline JS namepsace !
 */

Widgets.TimelineWidget = defclass("TimelineWidget", null, {
    __init__: function(wdgnode) {
        var tldiv = DIV({
            id: "tl",
            style: 'height: 200px; border: 1px solid #ccc;'
        });
        wdgnode.appendChild(tldiv);
        var tlunit = wdgnode.getAttribute('cubicweb:tlunit') || 'YEAR';
        var eventSource = new Timeline.DefaultEventSource();
        var bandData = {
            eventPainter: Timeline.CubicWebEventPainter,
            eventSource: eventSource,
            width: "100%",
            intervalUnit: Timeline.DateTime[tlunit.toUpperCase()],
            intervalPixels: 100
        };
        var bandInfos = [Timeline.createBandInfo(bandData)];
        this.tl = Timeline.create(tldiv, bandInfos);
        var loadurl = wdgnode.getAttribute('cubicweb:loadurl');
        Timeline.loadJSON(loadurl, function(json, url) {
            eventSource.loadJSON(json, url);
        });

    }
});

