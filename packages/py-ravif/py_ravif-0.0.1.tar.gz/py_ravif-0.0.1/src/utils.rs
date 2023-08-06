// From https://github.com/kornelski/cavif-rs/blob/main/src/main.rs
// Copyright (c) 2020, Kornel under BSD 3-Clause License

use imgref::ImgVec;
use rgb::RGBA8;

type BoxError = Box<dyn std::error::Error + Send + Sync>;

pub fn load_rgba(mut data: &[u8]) -> Result<ImgVec<RGBA8>, BoxError> {
  use rgb::FromSlice;

  let img = if data.get(0..4) == Some(&[0x89, b'P', b'N', b'G']) {
    let img = lodepng::decode32(data)?;
    ImgVec::new(img.buffer, img.width, img.height)
  } else {
    let mut jecoder = jpeg_decoder::Decoder::new(&mut data);
    let pixels = jecoder.decode()?;
    let info = jecoder.info().ok_or("Error reading JPEG info")?;
    use jpeg_decoder::PixelFormat::*;
    let buf: Vec<_> = match info.pixel_format {
      L8 => pixels
        .iter()
        .copied()
        .map(|g| RGBA8::new(g, g, g, 255))
        .collect(),
      RGB24 => {
        let rgb = pixels.as_rgb();
        rgb.iter().map(|p| p.alpha(255)).collect()
      }
      CMYK32 => return Err("CMYK JPEG is not supported. Please convert to PNG first".into()),
    };
    ImgVec::new(buf, info.width.into(), info.height.into())
  };
  Ok(img)
}
