var DjWebSocket = function(opts){
    var self = this;
    self.channels = {};
    var connect = function(uri){
        self.ws = new WebSocket(uri);
        self.ws.onopen = on_open;
        self.ws.onmessage = on_message;
        self.ws.onerror = on_error;
        self.ws.onclose = on_close;
    };

    var on_open = function(){
        if(self.onopen)self.onopen();
    }
    var on_message = function(data){
        var r = $.parseJSON(data.data);
        if($.isPlainObject(r)&& r['channel']){
            var fun = self.channels[r['channel']];
            if(fun){
                fun(r['content'])
            }

        }else{
            if(self.onmessage)self.onmessage(data);
        }


    }
    var on_error = function(){
        if(self.onerror)self.onerror();

    }
    var on_close = function(){
        if(self.onclose)self.onclose();
    }

    connect(opts.uri);


    self.send = function(data){
        self.ws.send(data)
    };

    self.subscribe = function(channel, fun){
        self.send($.param({channel: $.isArray(channel)?channel:[channel]}));
        self.channels[channel] = fun;
    };

    return self;
}