(import threading)
(import pudb)
(require processor.utils.macro)


(defn xmpp [jid password host &optional [port 5222] [recipients []]]
  (import-or-error [sleekxmpp [ClientXMPP]]
                   "Please, install 'sleekxmpp' library to use 'xmpp' source.")

  (defclass Bot [ClientXMPP]
    [[__init__ (fn [self jid password recipients]
                 (.__init__ (super Bot self) jid password)
                 (setv self.recipients recipients)
                 (self.add_event_handler "session_start" self.start))]
     
     [start (fn [self event]
              (self.send_presence)
              (self.get_roster))]
     
     [send_to_recipients (fn [self message recipients]
             (setv recipients (or recipients
                                  self.recipients))
             (for [recipient recipients]
               (print "SENDING MESSAGE")
               (apply self.send_message [] {"mto" recipient "mbody" message})))]])
  
  (setv bot (Bot jid password recipients))
  (bot.register_plugin "xep_0030") ;; Service Discovery
  (bot.register_plugin "xep_0199") ;; XMPP Ping


  (bot.connect [host port])
  (setv bot-thread (apply threading.Thread [] {"target" bot.process
                                                        "kwargs" {"block" True}}))
  (bot-thread.start)
  (print "BOT STARTED")
  ;; (apply bot.process [] {"block" False})

  ;; actual message sending function
  (fn [item]
    (bot.send_to_recipients (item.get "text" "Not given")
                            (item.get "recipients"))))

