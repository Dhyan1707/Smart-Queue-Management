'use client';

import { useEffect, useRef, useState } from 'react';
import { Html5Qrcode } from 'html5-qrcode';
import { X } from 'lucide-react';

interface QRScannerModalProps {
  onScanSuccess: (decodedText: string) => void;
  onClose: () => void;
}

export default function QRScannerModal({ onScanSuccess, onClose }: QRScannerModalProps) {
  const [error, setError] = useState<string | null>(null);
  const qrcodeRegionId = "html5qr-code-full-region";

  useEffect(() => {
    let html5QrCode: Html5Qrcode | null = null;
    let isMounted = true;

    const startScanner = async () => {
      try {
        html5QrCode = new Html5Qrcode(qrcodeRegionId);
        
        await html5QrCode.start(
          { facingMode: "environment" },
          {
            fps: 10,
            qrbox: { width: 250, height: 250 },
          },
          (decodedText) => {
            if (isMounted) {
              onScanSuccess(decodedText);
            }
          },
          (errorMessage) => {
            // Ignore parse errors as they are common when no QR is in frame
          }
        );
      } catch (err: any) {
        if (isMounted) {
          setError(err?.message || "Failed to start camera. Please ensure camera permissions are granted.");
        }
      }
    };

    startScanner();

    return () => {
      isMounted = false;
      if (html5QrCode && html5QrCode.isScanning) {
        html5QrCode.stop().then(() => {
          html5QrCode?.clear();
        }).catch(err => console.error("Failed to stop scanner", err));
      }
    };
  }, [onScanSuccess]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
      <div className="w-full max-w-md bg-slate-900 border border-slate-700 rounded-3xl overflow-hidden shadow-2xl relative">
        <div className="p-4 flex items-center justify-between border-b border-slate-800 bg-slate-900/50">
          <h3 className="text-lg font-bold text-white">Scan QR Code</h3>
          <button 
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-full transition-all"
          >
            <X className="h-5 w-5" />
          </button>
        </div>
        
        <div className="p-6 flex flex-col items-center">
          {error ? (
            <div className="text-rose-400 text-sm text-center p-4 bg-rose-500/10 rounded-xl border border-rose-500/30">
              {error}
            </div>
          ) : (
            <>
              <div id={qrcodeRegionId} className="w-full overflow-hidden rounded-2xl bg-black mb-4"></div>
              <p className="text-sm text-slate-400 text-center">
                Point your camera at the QR code to proceed.
              </p>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
