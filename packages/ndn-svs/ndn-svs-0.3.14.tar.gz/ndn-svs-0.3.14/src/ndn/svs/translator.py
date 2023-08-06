

# use plot


class SVSyncTranslator:
    translationsInPacket = 85
    def __init__(self, app:NDNApp, plotPrefix:Name, groupPrefix:Name, nid:Name, storage:Storage, secOptions:SecurityOptions) -> None:
        SVSyncLogger.info("SVSyncTranslator: started svsync translator")
        self.app, self.groupPrefix, self.nid, self.storage, self.secOptions, self.plots = app, groupPrefix, nid, storage, secOptions, {}
        self.plots[Name.to_str(nid)] = Plot(Name.to_str(nid))
        self.app.route(self.plotPrefix, need_sig_ptrs=True)(self.onPlotInterest)
        SVSyncLogger.info(f'SVSyncTranslator: started listening to {Name.to_str(self.plotPrefix)}')
    def getTranslation(nid:Name, seqno:int) -> Optional[Name]:
        try:
            map = self.maps[Name.to_str(nid)]
        except KeyError:
            return None
        return Name.from_str(map.find(seqno))
    def roundPlotno(plotno:int) -> int:
        return (plotno//self.translationsInPacket) if (plotno%self.translationsInPacket)>0 else (plotno//self.translationsInPacket)+1
    def onPlotInterest(self, int_name:FormalName, int_param:InterestParam, _app_param:Optional[BinaryStr], sig_ptrs:SignaturePtrs) -> None:
        nid, plotno = self.parsePlotName(int_name)
        # check storage
        data_pkt = self.storage.get_packet(int_name, int_param.can_be_prefix)
        if data_pkt:
            SVSyncLogger.info(f'SVSyncTranslator: served plot {Name.to_str(int_name)}')
            self.app.put_raw_packet(data_pkt)
        # check storage for next up
        rounded_name = self.getPlotName(nid, self.roundPlotno(plotno))
        data_pkt = self.storage.get_packet(rounded_name, int_param.can_be_prefix)
        if data_pkt:
            # do a forwarding hint
            SVSyncLogger.info(f'SVSyncTranslator: forwarding plot {Name.to_str(int_name)}')
            self.app.put_data(int_name, content=Name.to_bytes(rounded_name), content_type=ContentType.LINK)
    async def fetchPlot(self):
        pass
    def provideTranslation(seqno:int, label:str) -> None:
        pass
    def getPlotName(self, nid:Name, plotno:int) -> Name:
        return ( nid + self.groupPrefix + [Component.from_str("plot")] + [Component.from_str(str(plotno))] )
    def parsePlotName(self, int_name:FormalName) -> Tuple[Name,int]:
        raise NotImplementedError