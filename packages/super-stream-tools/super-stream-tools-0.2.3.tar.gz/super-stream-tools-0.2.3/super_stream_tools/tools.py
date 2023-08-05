import asyncio
from .stream_library import async_subprocess, save_file, delete_file
from typing import Optional, TypedDict
from enum import Enum
from os import name

is_windows = name == 'nt'


class arg_type(Enum):
    input_sources = 1
    mappings = 2
    metadata = 3
    args = 4


class interact_shell:
    def __init__(self) -> None:
        super().__init__()
        self.args = self.create_args()
        self.input_args = []

    async def execute(self) -> None:
        # await async_subprocess('pwd')
        await async_subprocess(*self.args, std_inputs=self.input_args)

    def add_argument(self, command: str, value: str | None = None, append_type: arg_type = arg_type.args, protect=False):
        x = self.__getattribute__(append_type.name)

        x.append('-'+command)
        if value:
            if protect:
                x.append(f'"{value}"')
            else:
                x.append(value)

    @staticmethod
    def create_args():
        return []


class ffmpeg(interact_shell):
    def __init__(self) -> None:
        super().__init__()
        self.input_sources = []
        self.mappings = []
        self.metadata = []

    @staticmethod  # overrides the parent method
    def create_args(args_list: list[str] = []):
        return ['ffmpeg'] + args_list


new_subtitle = TypedDict(
    'new_subtitle', {'url': str, 'lang': Optional[str]}, total=True
)


class encoder(ffmpeg):
    def __init__(self, hide_banner=True, accept_all_prompts=True, versbose_log_level='warning', overwrite_files=False, verbose=False) -> None:
        super().__init__()
        if hide_banner:
            self.add_argument('hide_banner')
        if not overwrite_files:
            self.add_argument('n')
        if overwrite_files and accept_all_prompts:
            self.input_args.append('y')
        if verbose:
            self.add_argument('loglevel', versbose_log_level)
        self.add_argument('reconnect', '1')
        self.add_argument('max_reload', '10')
        self.add_argument('reconnect_on_network_error', '1')
        self.add_argument('m3u8_hold_counters', '10')

    async def download(self, video_url: str, subtitles: list[new_subtitle] | None = None, output_file='test.mkv', program=0, audio_lang=None, thumbnail: str = None, execute=False):
        self.add_argument(
            'i', video_url, arg_type.input_sources, protect=is_windows)
        self.add_argument('map', f'0:p:{program}:v', arg_type.mappings)
        self.add_argument('map', f'0:p:{program}:a?', arg_type.mappings)
        idx = 0
        if subtitles:
            for idx, i in enumerate(subtitles):
                self.add_argument(
                    'i', i['url'], arg_type.input_sources, protect=is_windows)
                self.add_argument('map', str(idx+1), arg_type.mappings)

                if i['lang']:
                    self.add_argument(
                        f'metadata:s:s:{idx}', f"language={i['lang']}", arg_type.metadata)
        idx += 1
        if thumbnail:
            if 'http' in thumbnail:
                thumbnail = await save_file(thumbnail)
            self.add_argument('attach', thumbnail, arg_type.input_sources)
            self.add_argument(
                'metadata:s:t:0', 'mimetype="image/jpeg"', arg_type.input_sources)
            self.add_argument('metadata:s:t:0',
                              'filename=cover.jpg', arg_type.input_sources)
            if 'http' in thumbnail:
                delete_file()
        if audio_lang:
            self.add_argument('metadata:s:a:0',
                              f'language="{audio_lang}"', arg_type.metadata)

        self.args += self.input_sources
        # self.add_argument('codec', 'copy', arg_type.args)

        self.args += self.mappings
        self.args += self.metadata
        self.args.append(output_file)

        if execute:
            await self.execute()

    @staticmethod
    async def test():
        instance = encoder(overwrite_files=True, verbose=True)
        await instance.download(v,
                                [{'url': s1, 'lang': 'en-US'},
                                 {'url': s2, 'lang': 'es-ES'}],
                                program=5, thumbnail=t)
        print(instance.args)


if __name__ == '__main__':
    v = 'https://pl.crunchyroll.com/evs1/4d5ebef8c5e11efef476910028f49148/assets/oih0k1cp5uqyvui_,1890411.mp4,1890405.mp4,1890399.mp4,.urlset/master.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly9wbC5jcnVuY2h5cm9sbC5jb20vZXZzMS80ZDVlYmVmOGM1ZTExZWZlZjQ3NjkxMDAyOGY0OTE0OC9hc3NldHMvb2loMGsxY3A1dXF5dnVpXywxODkwNDExLm1wNCwxODkwNDA1Lm1wNCwxODkwMzk5Lm1wNCwudXJsc2V0L21hc3Rlci5tM3U4IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjQxOTcwMDU5fX19XX0_&Signature=osx7b1tHXQ1Hp9JZ4Wexz122YhkKyR2gZfBwgm0ePTE3y4UrHuYaezUEXdLFwW6U~OcVp9yLVtEm8n~pvLq01LREJHSHB55opJKGrEHsiuvFP8XhjDSZKFakMSrp0FSn-6XGfQ2InAYpRAAeIzpks4vk0pZNoz7EKq4G~MluZwPQeKwcM3m1OeXA9tW4taEq6bj2lCBWO9wfLi~GJTecb64qwzWO9Nbifb76XbMqlEAJHSFbb-ZXtSJaGnnrAp4R1ZrE7vKJlJeb7C7NsHA3QvZGfs4X0G~t0N9CpYZ1W96SZEBEerHw~Y0jd5VpylpaLmShVqkCB9Op7Wi3fTYm8A__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA'
    s1 = 'https://v.vrv.co/evs/4d5ebef8c5e11efef476910028f49148/assets/oih0k1cp5uqyvui_224899.txt?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly92LnZydi5jby9ldnMvNGQ1ZWJlZjhjNWUxMWVmZWY0NzY5MTAwMjhmNDkxNDgvYXNzZXRzL29paDBrMWNwNXVxeXZ1aV8yMjQ4OTkudHh0IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjQxOTcwMDYwfX19XX0_&Signature=Co4TXhK5Z-P6YbMhJnlJl1WMNhN9w9lNbb5zBX6O0FR1HEjeBpvFazXVIJaRHM1bCT~udxI8Yu2dyMDaMijyhvpJHPxtLbhu0GU-5HsSjTBbwgSNK~todT0IplemKD5FF77t7itsgnA1FlmB3WW2MktRGwawC3Ej1qAVgx2LHcgF3FTUEfKRUY4-eMbBaJUmxy9Tr05CD9FPY3wTFbNQU7sbAZ8~Y7~sf2BmrbS2Y3f7~MdGV5tnT34dsPpvIlhyYKniWcnE0mo1ehtQxMHlSioGvKbysXrWJ~uND8lwnE50FStqhHNU0v~2n7B7Qes836Vyd6b3LYxq2KTzk15neQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA'
    s2 = 'https://v.vrv.co/evs/4d5ebef8c5e11efef476910028f49148/assets/oih0k1cp5uqyvui_223754.txt?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly92LnZydi5jby9ldnMvNGQ1ZWJlZjhjNWUxMWVmZWY0NzY5MTAwMjhmNDkxNDgvYXNzZXRzL29paDBrMWNwNXVxeXZ1aV8yMjM3NTQudHh0IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjQxOTcwMDYwfX19XX0_&Signature=mT707cpKG~oZlS6Dhh33mKRvi20fsFzPd1ZNWPzyMZb3Y5zdo6uHfrz2aJLcUc9PzRwKTCH6blS8qObLKOz~i3IPDnOfQkNpticRHTmofaxYAPkUBn7lnKnvJ~vyLthwGHz4fLQml5D4I9hxxRkCeHlpztoBX78PbOPdjg4Fj0IqoIAv~Ww2Q3ftd4eG6m1nejDT3RKGZSJSpYcHtQ6zuGnbRX0HxgV4hbccZiYaoTKsURkYdE5c6UqbLocHa~b4KxgHHijMIDlrK9USqyW~RsXR~IeLEXN3pKwP4ciE9B9ty~J6Up35SYHMBKPx-7HnojjZj8iphVHyBjSdyNUMDQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA'
    t = 'https://beta.crunchyroll.com/imgsrv/display/thumbnail/1920x1080/catalog/crunchyroll/8bbc912efbdbcf655012d909904ff122.jpeg'
    asyncio.run(encoder.test())
