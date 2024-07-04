from kenar import (
    CreatePostAddonRequest,
    GetUserAddonsRequest,
    DeleteUserAddonRequest,
    GetPostAddonsRequest,
    DeletePostAddonRequest,
    CreateUserAddonRequest,
    IconName,
    Icon,
    TitleRow,
    SubtitleRow,
    SelectorRow,
    ScoreRow,
    LegendTitleRow,
    GroupInfo,
    EventRow,
    EvaluationRow,
    DescriptionRow,
    Color,
    WideButtonBar,
)

import divar_app
app = divar_app.app

POST_TOKEN = "gZFmMQKr"
ACCESS_TOKEN_HERE = "ory_at__ywH41CL1uzWZP67knIpkp9f3x6gq17HXBVmBcWM2gw.Lig8Btar7scjNHGjXbW0DvDjCWMk3tSA1Qwyj34fOo0"

if __name__ == "__main__":
    rsp = app.addon.upload_image("logo.png")
    image_name = rsp.image_name

    event_row = EventRow(
        title="سه بعدی",
        subtitle="فایل سه‌بعدی‌شو ببین",
        has_indicator=False,
        image_url=image_name,
        label="3d",
        has_divider=True,
        link=f"https://divar.azibom.com/?action=view&post_token={POST_TOKEN}",
        padded=True,
        icon=Icon(icon_name=IconName.ADD),
    )

    resp = app.addon.create_post_addon(
        access_token=ACCESS_TOKEN_HERE,
        data=CreatePostAddonRequest(
            token=POST_TOKEN,
            widgets=[
                event_row,
            ],
        ),
    )
    print(resp)