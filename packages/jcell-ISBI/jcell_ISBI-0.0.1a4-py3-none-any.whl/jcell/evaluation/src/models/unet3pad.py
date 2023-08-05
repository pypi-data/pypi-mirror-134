import torch
import torch.nn as nn

from ...src import save_defaults, load_defaults


class unet3pad(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(
        self, n_classes=2, is_deconv=False, in_channels=3, is_batchnorm=False
    ):
        super(unet3pad, self).__init__()
        self.is_deconv = is_deconv
        self.in_channels = in_channels
        self.is_batchnorm = is_batchnorm

        filters = [64, 128, 256, 512, 1024]

        self.down1 = unetDown(self.in_channels, filters[0], self.is_batchnorm)
        self.down2 = unetDown(filters[0], filters[1], self.is_batchnorm)
        self.down3 = unetDown(filters[1], filters[2], self.is_batchnorm)
        self.down4 = unetDown(filters[2], filters[3], self.is_batchnorm)
        self.center = unetConv2(filters[3], filters[4], self.is_batchnorm)
        self.up4 = unetUp(filters[4] + filters[3], filters[3], self.is_deconv)
        self.up3 = unetUp(filters[3] + filters[2], filters[2], self.is_deconv)
        self.up2 = unetUp(filters[2] + filters[1], filters[1], self.is_deconv)
        self.up1 = unetUp(filters[1] + filters[0], filters[0], self.is_deconv)
        self.final = nn.Conv3d(filters[0], n_classes, 1)

    def forward(self, inputs):
        x, befdown1 = self.down1(inputs)
        x, befdown2 = self.down2(x)
        x, befdown3 = self.down3(x)
        x, befdown4 = self.down4(x)
        x = self.center(x)
        x = self.up4(befdown4, x)
        x = self.up3(befdown3, x)
        x = self.up2(befdown2, x)
        x = self.up1(befdown1, x)

        return self.final(x)


class unetConv2(nn.Module):
    def __init__(self, in_size, out_size, is_batchnorm):
        super(unetConv2, self).__init__()

        if is_batchnorm:
            self.conv1 = nn.Sequential(
                nn.Conv3d(in_size, out_size, 3, 1, 1),
                nn.BatchNorm3d(out_size),
                nn.ReLU(),
            )
            self.conv2 = nn.Sequential(
                nn.Conv3d(out_size, out_size, 3, 1, 1),
                nn.BatchNorm3d(out_size),
                nn.ReLU(),
            )
        else:
            self.conv1 = nn.Sequential(
                nn.Conv3d(in_size, out_size, 3, 1, 1),
                nn.ReLU(),
            )
            self.conv2 = nn.Sequential(
                nn.Conv3d(out_size, out_size, 3, 1, 1),
                nn.ReLU(),
            )

    def forward(self, inputs):
        outputs = self.conv1(inputs)
        outputs = self.conv2(outputs)
        return outputs


class unetDown(nn.Module):
    def __init__(self, in_size, out_size, is_batchnorm):
        super(unetDown, self).__init__()
        self.conv = unetConv2(in_size, out_size, is_batchnorm)
        self.down = nn.MaxPool3d(2, 2)

    def forward(self, inputs):
        outputs = self.conv(inputs)
        outputs1 = self.down(outputs)
        return outputs1, outputs


class unetUp(nn.Module):
    def __init__(self, in_size, out_size, is_deconv):
        super(unetUp, self).__init__()
        self.conv = unetConv2(in_size, out_size, False)
        if is_deconv:
            self.up = nn.ConvTranspose3d(in_size, out_size, 2)
        else:
            self.up = nn.Upsample(scale_factor=2, mode="trilinear")

    def forward(self, inputs1, inputs2):
        outputs2 = self.up(inputs2)
        return self.conv(torch.cat([inputs1, outputs2], 1))
