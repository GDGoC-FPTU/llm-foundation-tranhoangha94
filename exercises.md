# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng, câu trả lời trở nên sáng tạo và đa dạng hơn. Ở `0.0` phản hồi sẽ rất cố định và ít biến thể, còn ở `1.5` nó dễ có thêm chi tiết bất ngờ hoặc cách diễn đạt khác lạ. Nói chung temperature thấp cho ra kết quả ổn định hơn, temperature cao cho ra nội dung phong phú và ít dự đoán trước hơn.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ chọn temperature thấp, khoảng `0.0` đến `0.5`, vì chatbot hỗ trợ khách hàng cần câu trả lời chính xác, nhất quán và ít rủi ro. Nếu temperature quá cao, model có thể trả về nội dung quá sáng tạo hoặc không nhất quán, làm giảm chất lượng trải nghiệm khách hàng.

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> Với chi phí token hiện tại, GPT-4o có tổng giá khoảng 25 USD trên 1 triệu token, trong khi GPT-4o-mini chỉ khoảng 0.75 USD trên 1 triệu token. Do đó GPT-4o đắt hơn GPT-4o-mini khoảng `33 lần` cho cùng workload token. Với 30.000 cuộc gọi và 350 token mỗi lần, chi phí hàng ngày sẽ là khoảng 262,5 USD cho GPT-4o so với khoảng 7,9 USD cho GPT-4o-mini.

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> GPT-4o là lựa chọn xứng đáng khi cần chất lượng và độ chính xác cao hơn, ví dụ như trả lời kỹ thuật, hỗ trợ khách hàng chuyên sâu, tóm tắt văn bản phức tạp hoặc nội dung mang tính chuyên môn. GPT-4o-mini phù hợp hơn cho các tác vụ khối lượng lớn, chi phí nhạy cảm, và yêu cầu không quá cao về độ chính xác, như chatbot FAQ đơn giản, phân loại nội dung cơ bản hoặc tạo nội dung ngắn cho trải nghiệm người dùng nhanh.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất khi người dùng tương tác trực tiếp và cần phản hồi nhanh, đặc biệt với nội dung dài hoặc trò chuyện theo từng bước, vì nó tạo cảm giác phản hồi tức thì và giảm cảm giác chờ đợi. Non-streaming phù hợp hơn khi câu trả lời ngắn, độ trễ không phải yếu tố chính, hoặc khi hệ thống chỉ cần xử lý batch/offline ở backend, vì cách này đơn giản hơn và dễ quản lý hơn.


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
