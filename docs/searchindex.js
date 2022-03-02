Search.setIndex({docnames:["CHANGELOG","README","copyright","index","modules","unicorn_binance_websocket_api"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["CHANGELOG.md","README.md","copyright.rst","index.rst","modules.rst","unicorn_binance_websocket_api.rst"],objects:{"":[[5,0,0,"-","unicorn_binance_websocket_api"]],"unicorn_binance_websocket_api.connection":[[5,1,1,"","BinanceWebSocketApiConnection"]],"unicorn_binance_websocket_api.connection.BinanceWebSocketApiConnection":[[5,2,1,"","close"],[5,2,1,"","receive"],[5,2,1,"","send"]],"unicorn_binance_websocket_api.manager":[[5,1,1,"","BinanceWebSocketApiManager"]],"unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager":[[5,2,1,"","add_to_ringbuffer_error"],[5,2,1,"","add_to_ringbuffer_result"],[5,2,1,"","add_to_stream_buffer"],[5,2,1,"","add_to_stream_signal_buffer"],[5,2,1,"","add_total_received_bytes"],[5,2,1,"","clear_stream_buffer"],[5,2,1,"","create_payload"],[5,2,1,"","create_stream"],[5,2,1,"","create_websocket_uri"],[5,2,1,"","delete_listen_key_by_stream_id"],[5,2,1,"","delete_stream_from_stream_list"],[5,2,1,"","fill_up_space_centered"],[5,2,1,"","fill_up_space_left"],[5,2,1,"","fill_up_space_right"],[5,2,1,"","get_active_stream_list"],[5,2,1,"","get_all_receives_last_second"],[5,2,1,"","get_binance_api_status"],[5,2,1,"","get_current_receiving_speed"],[5,2,1,"","get_current_receiving_speed_global"],[5,2,1,"","get_date_of_timestamp"],[5,2,1,"","get_errors_from_endpoints"],[5,2,1,"","get_event_loop_by_stream_id"],[5,2,1,"","get_exchange"],[5,2,1,"","get_human_bytesize"],[5,2,1,"","get_human_uptime"],[5,2,1,"","get_keep_max_received_last_second_entries"],[5,2,1,"","get_latest_release_info"],[5,2,1,"","get_latest_release_info_check_command"],[5,2,1,"","get_latest_version"],[5,2,1,"","get_latest_version_check_command"],[5,2,1,"","get_limit_of_subscriptions_per_stream"],[5,2,1,"","get_listen_key_from_restclient"],[5,2,1,"","get_monitoring_status_icinga"],[5,2,1,"","get_monitoring_status_plain"],[5,2,1,"","get_most_receives_per_second"],[5,2,1,"","get_new_stream_id"],[5,2,1,"","get_number_of_all_subscriptions"],[5,2,1,"","get_number_of_free_subscription_slots"],[5,2,1,"","get_number_of_streams_in_stream_list"],[5,2,1,"","get_number_of_subscriptions"],[5,2,1,"","get_process_usage_cpu"],[5,2,1,"","get_process_usage_memory"],[5,2,1,"","get_process_usage_threads"],[5,2,1,"","get_reconnects"],[5,2,1,"","get_request_id"],[5,2,1,"","get_result_by_request_id"],[5,2,1,"","get_results_from_endpoints"],[5,2,1,"","get_ringbuffer_error_max_size"],[5,2,1,"","get_ringbuffer_result_max_size"],[5,2,1,"","get_start_time"],[5,2,1,"","get_stream_buffer_byte_size"],[5,2,1,"","get_stream_buffer_length"],[5,2,1,"","get_stream_buffer_maxlen"],[5,2,1,"","get_stream_id_by_label"],[5,2,1,"","get_stream_info"],[5,2,1,"","get_stream_label"],[5,2,1,"","get_stream_list"],[5,2,1,"","get_stream_receives_last_second"],[5,2,1,"","get_stream_statistic"],[5,2,1,"","get_stream_subscriptions"],[5,2,1,"","get_total_received_bytes"],[5,2,1,"","get_total_receives"],[5,2,1,"","get_used_weight"],[5,2,1,"","get_user_agent"],[5,2,1,"","get_version"],[5,2,1,"","get_version_unicorn_fy"],[5,2,1,"","help"],[5,2,1,"","increase_processed_receives_statistic"],[5,2,1,"","increase_received_bytes_per_second"],[5,2,1,"","increase_reconnect_counter"],[5,2,1,"","increase_transmitted_counter"],[5,2,1,"","is_exchange_type"],[5,2,1,"","is_manager_stopping"],[5,2,1,"","is_stop_as_crash_request"],[5,2,1,"","is_stop_request"],[5,2,1,"","is_update_availabe"],[5,2,1,"","is_update_availabe_check_command"],[5,2,1,"","is_update_availabe_unicorn_fy"],[5,2,1,"","kill_stream"],[5,2,1,"","pop_stream_data_from_stream_buffer"],[5,2,1,"","pop_stream_signal_from_stream_signal_buffer"],[5,2,1,"","print_stream_info"],[5,2,1,"","print_summary"],[5,2,1,"","print_summary_to_png"],[5,2,1,"","remove_ansi_escape_codes"],[5,2,1,"","replace_stream"],[5,2,1,"","run"],[5,2,1,"","set_heartbeat"],[5,2,1,"","set_keep_max_received_last_second_entries"],[5,2,1,"","set_private_dex_config"],[5,2,1,"","set_restart_request"],[5,2,1,"","set_ringbuffer_error_max_size"],[5,2,1,"","set_ringbuffer_result_max_size"],[5,2,1,"","set_stream_label"],[5,2,1,"","split_payload"],[5,2,1,"","start_monitoring_api"],[5,2,1,"","stop_manager_with_all_streams"],[5,2,1,"","stop_monitoring_api"],[5,2,1,"","stop_stream"],[5,2,1,"","stop_stream_as_crash"],[5,2,1,"","stream_is_crashing"],[5,2,1,"","stream_is_stopping"],[5,2,1,"","subscribe_to_stream"],[5,2,1,"","unsubscribe_from_stream"],[5,2,1,"","wait_till_stream_has_started"],[5,2,1,"","wait_till_stream_has_stopped"]],"unicorn_binance_websocket_api.restclient":[[5,1,1,"","BinanceWebSocketApiRestclient"]],"unicorn_binance_websocket_api.restclient.BinanceWebSocketApiRestclient":[[5,2,1,"","delete_listen_key"],[5,2,1,"","get_listen_key"],[5,2,1,"","keepalive_listen_key"]],"unicorn_binance_websocket_api.restserver":[[5,1,1,"","BinanceWebSocketApiRestServer"]],"unicorn_binance_websocket_api.restserver.BinanceWebSocketApiRestServer":[[5,2,1,"","get"],[5,3,1,"","methods"]],"unicorn_binance_websocket_api.sockets":[[5,1,1,"","BinanceWebSocketApiSocket"]],"unicorn_binance_websocket_api.sockets.BinanceWebSocketApiSocket":[[5,2,1,"","start_socket"]],unicorn_binance_websocket_api:[[5,0,0,"-","connection"],[5,0,0,"-","manager"],[5,0,0,"-","restclient"],[5,0,0,"-","restserver"],[5,0,0,"-","sockets"]]},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute"},terms:{"0":[1,3,5],"04":0,"1":[1,3,5],"10":[3,5],"100":1,"101":0,"1011":5,"1024":0,"1042747365":0,"109":0,"11":3,"110":0,"111":0,"119":0,"12":[3,5],"121":0,"127":[0,5],"13":3,"131":0,"136":0,"14":3,"142":0,"143":0,"148":0,"15":3,"16":3,"160":0,"161":0,"162":0,"163":0,"164":0,"167":0,"17":3,"176":0,"18":3,"189":0,"19":3,"190":0,"195":0,"199":0,"1m":1,"1s":1,"2":[3,5],"20":[3,5],"200":0,"2015":0,"2019":2,"2020":0,"2022":2,"206":0,"208":0,"209":0,"21":3,"22":3,"221":0,"223":0,"224":0,"23":3,"235":0,"237":0,"24":3,"243":0,"25":3,"26":3,"27":3,"28":3,"29":3,"2nd":0,"3":3,"30":3,"30m":5,"31":3,"32":3,"33":3,"34":3,"35":[1,3],"350":5,"36":3,"37":3,"4":[3,5],"40":0,"400":0,"414":0,"43":0,"45":0,"47":0,"48":0,"5":[3,5],"50":0,"51":0,"590914274":0,"5fccfd572db2f530e25e302c02be5dec12759cf9":0,"6":[3,5],"60":0,"61":5,"64201":5,"7":[1,3],"72":0,"8":3,"8000":5,"8004":0,"84":0,"87":0,"9":3,"95":0,"96":0,"97":0,"98":0,"byte":5,"case":0,"catch":0,"char":[0,5],"class":[0,5],"default":[0,5],"do":[1,2],"export":[0,5],"final":5,"function":[0,5],"import":[1,3],"int":5,"long":0,"new":[0,3,5],"public":1,"return":[0,5],"short":[0,5],"static":5,"throw":0,"true":[0,1,5],"try":[0,1],"var":5,"while":[0,1],A:[2,3,5],AND:2,AS:2,And:3,BE:2,BUT:2,Be:1,But:5,FOR:2,IN:2,IS:2,If:[0,1,5],Is:5,It:[0,5],Its:0,NO:2,NOT:2,No:[0,1],OF:2,OR:2,THE:2,TO:2,That:0,The:[0,1,2,5],There:5,To:[1,5],WITH:2,_:[0,1],__init__:0,_add_socket_to_socket_list:0,_add_stream_to_stream_list:0,_create_stream_thread:0,_frequent_check:0,_keepalive_stream:0,_request:0,_restart_stream:0,aaa:5,abl:[0,1],about:[0,1,2,5],abov:[1,2],accept:0,account:5,accur:0,acquir:5,action:2,activ:[0,5],active_stream:5,ad:[3,5],add:[0,5],add_str:[0,5],add_to_ringbuffer_error:[0,5],add_to_ringbuffer_result:[0,5],add_to_stream_buff:5,add_to_stream_signal_buff:5,add_total_received_byt:5,address:[1,5],adher:0,aenter:0,after:[0,5],again:[0,1],agent:0,alert:0,aliv:5,all:[0,1,2,5],allow:5,allwai:0,alreadi:0,also:[0,1,5],alwai:[0,5],amount:[0,5],an:[0,1,2,5],ani:2,ankrbtc:5,announc:1,ansi:5,anymor:0,anyth:1,api:5,api_kei:[0,1,5],api_secret:[0,1,5],apidoc:5,applic:1,appreci:1,ar:[0,3,5],arbitrari:5,archiv:1,argument:0,aris:2,arr:[0,5],arrai:0,assign:0,associ:2,async:5,asynchron:1,asyncio:[0,1,5],attr:0,attribut:0,attributeerror:0,austria:1,author:2,auto:[0,1],automat:5,avail:[0,1,5],availab:0,averag:5,average_receives_per_second:5,average_receiving_spe:0,average_speed_per_second:5,avoid:[0,1,5],awar:1,back:[1,5],bad:0,ban:[0,1],base:[0,5],base_futur:0,bash:1,basic:1,bbb:5,becaus:[0,5],befor:[0,1,5],behavior:5,behaviour:0,belong:0,below:1,benefit:3,better:0,bin:0,binanc:5,binance_api_statu:0,binance_com_websocket:1,binance_dex_user_address:5,binance_websocket_api_manag:5,binancedexchang:1,binanceexchang:1,binancewebsocketapiconnect:[0,5],binancewebsocketapimanag:[0,1,5],binancewebsocketapirestcli:[0,5],binancewebsocketapirestserv:5,binancewebsocketapisocket:5,bind:1,blank:[0,5],blind:5,blob:[0,5],blockheight:1,bnbbtc:[1,5],boarder:0,booktick:[0,1,5],bool:5,bosma:0,bot:5,bound:5,branch:1,btcusdt:1,buffer:[0,1,5],bug:[0,3],buggi:0,build:3,bump:0,bypass:0,c:[1,2],cach:[0,5],calcul:5,call:[0,5],callback:[0,1],can:[0,1,5],cannot:0,card:0,caus:[0,1,5],ceas:0,center:0,central:5,cex:[0,5],chain:[0,1,5],chang:[3,5],changelog:[0,1,3],channel:[0,3,5],charg:2,check:[0,1,5],check_command:5,check_command_vers:5,check_lucit_collector:5,checkcommandvers:5,choos:5,claim:2,clean:0,clear:[0,5],clear_stream_buff:[0,5],click:1,client:[0,5],close:[0,5],close_timeout:[0,5],code:[0,3,5],codeql:0,coin:[0,1],coin_futur:[1,5],cointain:5,collect:[0,5],color:0,colorama:5,com:[0,1,5],combin:[1,5],come:0,command:[0,1],comment:0,commerci:3,commun:1,compani:1,compat:[0,1],complet:[1,5],compositeindex:1,compress:0,comput:1,concurr:1,conda:3,condit:2,config:[0,5],configur:[0,1],conncect:0,connect:[0,2,3,4],connnect:0,consid:[1,5],consist:[1,5],consol:5,consult:1,contact:1,content:[0,4],contract:2,contribut:3,contributor:3,control:[0,1,5],convert:[0,3,5],copi:2,copyright:[2,3],coroutin:0,correctli:0,correspond:5,cost:0,count:0,counter:[0,5],cpu:[0,5],crash:[0,5],crashed_stream:5,creat:[0,3,5],create_payload:[0,5],create_stream:[0,1,5],create_websocket_uri:[0,5],creation:0,critic:[0,5],ctrl:1,curl:1,currenc:0,current:[0,1,5],current_receiving_spe:0,curs:5,daemon:1,dai:5,damag:2,data:[0,3,5],data_record:5,databas:[0,5],date:5,dawe35:0,dead:1,deal:[1,2],debug:5,decentr:5,decim:0,decod:0,defin:[0,5],del:0,delet:[0,5],delete_listen_kei:5,delete_listen_key_by_stream_id:[0,5],delete_stream_from_stream_list:5,deliv:5,demand_of_char:5,demo:3,depend:[0,1],deprec:0,depth5:1,depth:1,dequ:0,descript:[0,3,5],determin:1,dev:3,develop:[1,2,3,5],dex:[0,1,5],di:0,dict:[0,5],dictionari:3,did:0,didnt:0,differ:[0,1,5],direct:0,disabl:5,disable_colorama:[0,5],disable_print:[0,5],discard:5,disconnect:[0,1,5],discov:1,discuss:[0,1],distribut:2,doc:[0,1,5],docstr:0,document:[0,2,5],doe:[0,5],doesn:0,done:[0,5],dont:[0,1,5],doubl:0,download:1,drop:0,dstream:0,dure:[0,1,5],e:5,each:[0,1],easi:[1,5],element:5,en:[1,5],enabl:5,enable_stream_signal_buff:5,end:5,endpoint:[0,1,5],engbtc:1,english:1,ensur:[0,5],entri:5,environ:3,error:[0,1,5],error_msg:5,especi:5,estim:5,ethbtc:[1,5],even:[1,5],event:[0,2,5],event_loop:0,everi:[0,5],everyon:1,everyth:[0,1],exampl:[0,3,5],excap:5,exce:0,exceed:[0,5],except:[0,5],excess:1,exchang:[0,1,5],exchange_typ:5,exclude_kill_request:5,execut:0,exist:[1,5],expcept:0,expect:0,explain:1,explor:1,express:2,extend:[0,1],facebook:1,fail:3,failur:0,fals:[0,5],fast:[1,5],feasibl:0,featur:[0,1,5],few:[0,5],fifo:[0,1,5],file:[0,2,5],fill:[0,5],fill_up_spac:0,fill_up_space_cent:5,fill_up_space_left:[0,5],fill_up_space_right:[0,5],find:1,fine:0,first:[0,5],first_received_data:[0,1,5],fit:2,fix:[1,3],flap:0,flask_rest:5,flexibl:[1,5],flowelcat:0,flush:5,folder:0,follow:[1,2],forceord:[1,5],form:3,format:[0,1,5],forward:0,frame:5,free:[2,5],frequent:0,frequent_checks_list:0,frequentcheck:0,from:[0,2,3,5],full:5,fulli:[1,5],fund:1,furnish:2,further:0,futur:[0,1,5],fy:1,g:5,gener:[0,1,5],get:[0,3,5],get_active_stream_list:5,get_all_receives_last_second:5,get_binance_api_statu:[0,1,5],get_current_receiving_spe:[1,5],get_current_receiving_speed_glob:[0,5],get_date_of_timestamp:5,get_errors_from_endpoint:[0,1,5],get_event_loop_by_stream_id:[0,5],get_exchang:5,get_human_bytes:5,get_human_uptim:5,get_keep_max_received_last_second_entri:5,get_latest_release_info:5,get_latest_release_info_check_command:5,get_latest_vers:5,get_latest_version_check_command:5,get_limit_of_subscriptions_per_stream:[0,1,5],get_listen_kei:[0,5],get_listen_key_from_restcli:5,get_monitoring_status_icinga:[0,5],get_monitoring_status_plain:[0,1,5],get_most_receives_per_second:5,get_new_stream_id:[0,5],get_number_of_all_subscript:[0,5],get_number_of_free_subscription_slot:[0,5],get_number_of_streams_in_stream_list:5,get_number_of_subscript:5,get_process_usage_cpu:[0,5],get_process_usage_memori:[0,5],get_process_usage_thread:[0,5],get_reconnect:5,get_request_id:[1,5],get_result_by_request_id:[0,1,5],get_results_from_endpoint:[0,1,5],get_ringbuffer_error_max_s:[0,5],get_ringbuffer_result_max_s:[0,5],get_start_tim:5,get_stream_buffer_byte_s:[0,5],get_stream_buffer_length:[0,1,5],get_stream_buffer_maxlen:[0,5],get_stream_id_by_label:[0,1,5],get_stream_info:[1,5],get_stream_label:[0,5],get_stream_list:[1,5],get_stream_receives_last_second:5,get_stream_statist:[1,5],get_stream_subscript:[0,1,5],get_total_rec:5,get_total_received_byt:5,get_used_weight:[0,5],get_user_ag:[0,5],get_vers:[1,5],get_version_unicorn_fi:[0,5],get_websocket_uri_length:0,getlogg:1,github:[0,3,5],global:0,globali:5,go:[0,5],good:5,got:5,graceful:0,grant:2,grep:1,gronastech:0,group:1,grow:5,guid:1,guidelin:1,gz:1,ha:[0,5],had:0,hammer:0,handl:[0,1,5],handler:[0,5],handler_binance_websocket_api_manag:5,handshak:5,hard:5,have:[0,5],heal:5,heartbeat:5,help:[0,1,5],here:1,herebi:2,high:0,higher:0,highest:5,highest_receiving_spe:0,hight:5,hight_per_row:5,histori:1,holder:2,homepag:3,host:5,hour:[0,5],how:[3,5],howto:3,html:[1,5],http:[0,1,2,5],human:5,i:0,icinga2:1,icinga:[0,1,5],id:5,identifi:5,imag:[0,5],immedi:0,implement:0,impli:2,improv:[0,3],inact:5,includ:[0,2,5],increas:5,increase_processed_receives_statist:5,increase_received_bytes_per_second:5,increase_reconnect_count:5,increase_transmitted_count:[0,5],independ:5,index:3,indexerror:0,individu:0,inf:5,info:[3,5],inform:5,init:0,initi:[1,5],insid:[0,5],inspect:1,instal:[0,3],instanc:[0,1,5],instead:[0,5],interact:1,internet:0,interpret:0,interrupt:5,interv:0,introduc:0,introspect:1,invalid:[0,5],invalidmessag:0,invalidstateerror:0,invalidstatuscod:0,io:5,ip:5,ipython:[1,5],is_exchange_typ:[0,5],is_manager_stop:5,is_stop_as_crash_request:[0,5],is_stop_request:5,is_update_availab:[1,5],is_update_availabe_check_command:5,is_update_availabe_unicorn_fi:[0,5],is_websocket_uri_length_valid:0,isn:5,isol:[0,1,5],isolated_margin:[1,5],issu:[0,1,5],issuecom:0,item:[0,5],iter:0,its:[0,5],itself:5,je:[0,5],jersei:0,jex:[0,1,5],jexapi:5,json:0,jsondecodeerror:0,jupyt:1,just:[3,5],k:1,keep:[0,5],keepal:[0,5],keepalive_listen_kei:5,keepalive_streams_id:0,keepalive_streams_list:0,kei:[0,1,5],kept:5,keyerror:0,kick:[1,5],kill:5,kill_request:5,kill_stream:5,kind:[2,5],kline:[0,1],kline_12h:1,kline_15m:1,kline_1:5,kline_1h:1,kline_1m:1,kline_30m:1,kline_5m:[1,5],known:[0,1],label:[0,5],last:[1,5],last_received_data_record:0,last_static_ping_listen_kei:5,latest:[0,3,5],lead:5,learn:1,left:5,len:[0,5],length:[0,5],less:0,level:0,liabil:2,liabl:2,lib:[0,1,5],librari:5,lifo:[0,1,5],like:[0,1,5],limit:[0,2,5],line:[0,3],link:[0,1],linux:5,list:[0,1,5],listen:[0,5],listen_kei:[0,5],listenkei:[0,5],live:3,local:0,lock:0,log:[3,5],logfil:0,logger:[0,3],loglevel:0,longer:0,look:[1,5],loop:[0,5],lordofseren:0,loss:5,lost:5,lower:0,lucit:[0,1,2,5],m3tz3l:0,m:1,mac:[0,1],mai:5,mainten:1,make:[0,5],manag:[0,1,3,4],mani:[0,1,5],margin:[0,1,5],market:[0,3,5],marketdepth:5,master:[0,1,5],max:[0,1,5],max_items_per_request:5,max_siz:5,max_subscriptions_per_stream:0,maximum:5,maxlen:[0,5],mayb:0,md:[0,5],me:[1,2],measur:0,media:1,memori:[0,5],merchant:2,merg:2,messag:[0,5],method:[0,5],metric:5,migrat:1,min:0,minitick:[0,1,5],minut:1,miss:0,mode:[0,1,5],modifi:2,modul:[0,1,3,4],modyfi:0,monitor:[0,1,5],monitoring_api_serv:0,more:[0,3,5],most:0,move:0,msg:[0,5],much:5,multi:1,multipl:1,multiplex:[0,3,5],must:[0,5],mutabl:0,my:1,nagio:[1,5],name:[0,5],need:[0,1,5],negotiationerror:0,network:0,new_api_kei:5,new_api_secret:5,new_channel:5,new_close_timeout:5,new_market:5,new_output:[0,5],new_ping_interv:5,new_ping_timeout:5,new_stream_buffer_maxlen:5,new_stream_buffer_nam:5,new_stream_id:5,new_stream_label:5,new_symbol:5,nice:[0,1],node:0,non:[1,5],none:[0,5],noninfring:2,normal:[1,5],notabl:0,notebook:1,notic:2,notif:3,now:0,number:[0,5],number_of_max_entri:5,object:5,obsolet:5,obtain:2,offer:1,offici:[0,5],offlin:0,often:0,ok:5,old:5,oldest:5,oldest_data_from_stream_buff:1,oliv:[0,2],onc:[1,5],one:[0,1,5],onli:[0,5],op:1,open:[0,1,5],oper:[0,1],opposit:5,option:[1,5],order:[1,5],org:[0,1,5],os:[0,1,5],oserror:0,other:[0,2,5],otherwis:[2,5],out:2,outdat:0,output:[0,1,5],output_default:[0,5],overload:5,overrul:5,overview:[1,5],overwritten:5,own:[0,1],packag:[0,1,3,4],page:[0,3],panda:1,param:5,paramet:[0,1,5],part:[0,1],partial:0,particular:2,pass:5,path:[0,5],pathlib:0,payload:[0,5],peak:0,per:[0,1,5],perfdata:[0,5],permiss:2,permit:2,perpetu:0,person:2,pick:1,ping:[0,5],ping_interv:[0,5],ping_timeout:[0,5],pip:3,pipe:5,place:0,plai:0,plain:[0,3,5],plan:[1,5],platform:0,plattform:0,pleas:[1,3,5],plot:1,png:[0,5],pong:5,pop:0,pop_stream_data_from_stream_buff:[0,1,5],pop_stream_signal_from_stream_signal_buff:5,port:5,portion:2,possibl:[0,1,5],post:0,power:5,pr:0,pre:0,presenc:5,price:1,print:[0,3,5],print_stream_info:[0,5],print_suammari:0,print_summari:[0,1,5],print_summary_export_path:[0,5],print_summary_to_png:5,privat:[0,1],process:[0,1,5],process_stream_data:5,process_stream_sign:[0,5],product:0,project:[0,3],propper:0,protect:1,provid:[0,1,2,5],proxi:5,psutil:0,publish:2,pull:0,purpos:2,push:0,py:[0,1,5],pypi:[0,3],python:[0,3,5],quantiti:0,rais:0,ram:1,raw:[3,5],raw_data:5,raw_stream_data:5,reach:0,read:[3,5],readabl:5,readm:[0,3],real:0,reason:0,receiv:[0,3,5],received_last_second:5,receives_statistic_last_second:0,receiving_speed_peak:0,recent:0,recogn:[0,5],recommend:[3,5],reconnect:[0,1,5],record:[0,5],refer:[0,5],referenc:0,reformat:0,refresh:1,relat:[1,5],releas:[0,3,5],remain:5,remot:5,remov:[3,5],remove_ansi_escape_cod:5,renam:0,repair:0,replac:[0,5],replace_stream:[0,1,5],repo:1,report:[0,3,5],repositori:[0,1],reproduc:1,request:[0,5],request_id:[0,5],requir:[0,1],reset:0,resourc:5,respect:1,respond:0,respons:5,rest:[0,1,5],restart:[0,5],restart_stream:0,restart_timeout:[0,5],restarting_stream:5,restclient:[0,3,4],restor:5,restrict:2,restserv:[3,4],result:[0,5],return_cod:[0,5],rewrit:3,rewritten:0,rich:1,right:[0,2,3,5],ringbuff:5,robust:[1,5],round:0,routin:0,row:[0,5],run:[0,1,5],runtimeerror:0,runtimeexcept:0,runtimewarn:0,s1:0,s:[1,5],safe:0,save:[0,5],scope:0,script:1,search:[3,5],second:[0,5],secret:[0,1,5],secur:[0,1],see:[0,5],seem:0,select:5,self:0,sell:2,semant:0,send:[0,5],sensit:0,sent:5,separ:[0,1],serv:5,server:5,servic:[1,5],set:[0,1,5],set_heartbeat:[0,5],set_keep_max_received_last_second_entri:5,set_private_api_config:0,set_private_dex_config:5,set_restart_request:5,set_ringbuffer_error_max_s:[0,1,5],set_ringbuffer_result_max_s:[0,5],set_stream_label:[0,1,5],setup:1,sh:0,shall:2,share:[0,5],shell:1,should:[1,5],show:[0,5],show_secrets_in_log:[0,5],shutdown:[0,5],side:5,signal:[0,1,5],signal_typ:5,simpl:1,simplejson:0,sinc:[0,5],singl:[0,5],size:[0,5],slash:0,sleep:0,slot:5,so:[0,1,2,5],social:3,socket:[0,3,4],socket_id:5,softwar:2,some:0,someth:5,soon:5,sourc:3,space:[0,5],specif:[0,1,5],specifi:[0,5],speed:[0,5],split:5,split_payload:[0,5],spot:[0,5],ssl:0,sslerror:0,stabl:1,stack:[0,5],stage:3,stai:5,start:[0,1,5],start_monitoring_api:[0,5],start_socket:[0,5],start_tim:5,stateless:0,statist:5,statu:[0,1,5],status_cod:5,status_text:5,statusformat:5,still:1,stock:0,stop:[0,5],stop_as_crash_request:5,stop_manager_with_all_stream:[1,5],stop_monitoring_api:5,stop_request:5,stop_stream:[0,1,5],stop_stream_as_crash:[0,5],stopped_stream:5,store:[1,5],str:[0,5],stream:[0,1,5],stream_buff:[0,1,5],stream_buffer_item:5,stream_buffer_maxlen:[0,5],stream_buffer_mb:5,stream_buffer_nam:5,stream_data:5,stream_id:[0,1,5],stream_is_crash:5,stream_is_stop:5,stream_label:[0,5],stream_list:[0,5],stream_sign:5,stream_signal_buff:[0,1,5],streambuff:0,streamrecoveryerror:0,string:[0,1,5],style:1,subject:2,sublicens:2,submodul:[3,4],subscrib:[0,3,5],subscribe_from_stream:0,subscribe_to_stream:[1,5],subscript:[0,1,5],substanti:2,success:5,suffix:5,suggest:3,suit:1,summari:0,support:[0,3,5],swiftbar:0,symbol:[0,5],syntax:1,system:[0,1,2,5],t:[0,1,5],ta:1,tab:[0,1],tag_nam:1,take:[1,5],tar:1,tarbal:1,tcp:5,tech:[1,2],technic:1,telegram:1,temporari:1,termin:5,test:[0,1],testnet:[0,1,5],text:[0,5],than:[0,5],thank:0,thei:[0,5],them:[0,1],thi:[0,1,2,5],thread:[0,1,5],through:5,throw_exception_if_unrepair:[0,5],thrown:0,thx:0,ticker:[0,1,5],tidi:5,till:[1,5],time:[0,5],timeout:[0,5],timeouterror:0,timespan:5,timestamp:[0,5],todo:0,too:0,took:0,tool:0,top:0,topic:1,tort:2,total:5,total_received_length:0,total_received_mb:5,total_receiving_spe:0,tr:1,trace:1,trade:[1,5],trail:0,transfer:5,transmit:5,trbinanc:[0,1,5],tune:0,tupl:[0,5],twist:1,twitter:1,two:[0,5],txt:1,type:[0,5],typeerror:0,typo:0,ubwa:[0,1],uggel:0,ujson:0,unboundlocalerror:0,unchang:[1,5],under:5,unicorn:5,unicorn_binance_websocket_api:[1,3],unicorn_binance_websocket_api_connect:0,unicorn_binance_websocket_api_except:0,unicorn_binance_websocket_api_manag:0,unicorn_binance_websocket_api_socket:0,unicorn_fi:5,unicorn_fied_stream_data:1,unicorndev:1,unicornfi:[0,3,5],uniqu:5,unknown:[0,5],unknownexchang:0,unoffici:[1,5],unreleas:3,unrepair:5,unstabl:3,unsubscrib:[0,3,5],unsubscribe_from_stream:[1,5],unus:[0,5],up:[0,1,5],updat:[1,3,5],update_msg:5,upgrad:3,upper:0,uppercas:0,uptim:5,uri:[0,5],url:0,us:[0,1,2,5],usa:1,usag:0,usd:1,used_weight:5,user:[0,1,5],user_address:5,user_ag:5,user_data:5,userdata:[0,1,5],userdatastream:0,utc:0,uuid:[0,5],valid:[0,1,5],valu:[0,5],valueerror:0,variabl:[0,5],venv:0,veri:0,version:[0,1,5],via:[0,1,5],vienna:1,view:5,virtualenv:3,vision:[1,5],wa:0,wai:[1,5],wait:[0,5],wait_till_stream_has_start:[1,5],wait_till_stream_has_stop:5,want:[1,5],warn:[0,5],warn_on_upd:[0,5],warranti:2,watch:1,we:[0,1],web:5,websocket:5,websockets10:0,webstream:[3,5],weight:0,welcom:1,well:3,what:3,wheel:3,when:[0,5],where:5,whether:2,which:[0,1,5],whitespac:5,whom:2,wiki:[3,5],window:0,wish:5,withdraw:1,within:[1,5],without:[0,2],work:[0,5],would:1,write:[1,5],written:[0,5],wrong:[0,5],ws:[0,5],wss:[0,5],www:[0,1,2,5],xxx:0,yml:1,you:[0,1,5],your:[1,5],zehentleitn:[0,2],zileth:1},titles:["unicorn-binance-websocket-api Change Log","UNICORN Binance WebSocket API","MIT License","Welcome to unicorn-binance-websocket-api\u2019s documentation!","unicorn_binance_websocket_api","unicorn_binance_websocket_api package"],titleterms:{"0":0,"1":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"2":0,"20":0,"21":0,"22":0,"23":0,"24":0,"25":0,"26":0,"27":0,"28":0,"29":0,"3":[0,1],"30":0,"31":0,"32":0,"33":0,"34":0,"35":0,"36":0,"37":0,"4":[0,1],"5":0,"6":0,"7":0,"8":0,"9":0,"import":0,"new":1,A:1,And:1,ad:0,api:[0,1,3],ar:1,benefit:1,binanc:[0,1,3],bug:1,build:0,chang:[0,1],channel:1,code:1,commerci:1,conda:1,connect:[1,5],content:[3,5],contribut:1,contributor:1,convert:1,creat:1,data:1,demo:1,descript:1,dev:[0,1],develop:0,dictionari:1,document:[1,3],environ:1,exampl:1,fail:0,fix:0,form:1,from:1,get:1,github:1,homepag:1,how:1,howto:1,improv:1,indic:3,info:0,instal:1,just:1,latest:1,licens:2,line:1,linux:1,live:1,log:[0,1],logger:1,maco:1,manag:5,market:1,mit:2,modul:5,more:1,multiplex:1,notif:1,packag:5,pip:1,plain:1,pleas:0,print:1,project:1,pypi:1,python:1,raw:1,read:0,receiv:1,recommend:0,releas:1,remov:0,report:1,restclient:5,restserv:5,rewrit:0,right:1,s:3,social:1,socket:5,sourc:1,stage:[0,1],submodul:5,subscrib:1,suggest:1,support:1,tabl:3,unicorn:[0,1,3],unicorn_binance_websocket_api:[4,5],unicornfi:1,unreleas:0,unstabl:0,unsubscrib:1,updat:0,upgrad:1,virtualenv:1,websocket:[0,1,3],webstream:1,welcom:3,well:1,what:1,wheel:1,wiki:1,window:1}})